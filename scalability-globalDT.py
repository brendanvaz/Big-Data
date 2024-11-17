import sys
import time

"""
    This program will allow us to re-run the same experiment with spam-base, modifying the number of cores, the size of the data used as input. As such, many parts of the code as 'fixed' for the specific dataset. 

    We will only run the building phase, 

    Param 1: Number of Cores/Partitions
    Param 2: Percentage of the training data to use

"""

from src.transforms.Preprocessing import CleanTweet, polarityCalculator
from pyspark.ml.feature import (
    RegexTokenizer,
    StopWordsRemover,
    CountVectorizer,
    IDF,
    StringIndexer,
)
from pyspark.ml.classification import LogisticRegression
from pyspark.ml import Pipeline


def pipelineCv():
    cleanTweet = CleanTweet()
    regexTokenizer = RegexTokenizer(
        inputCol="cleaned_tweet",
        outputCol="cleaned_tweet_words",
        pattern="[^a-zA-Z0-9_#]",
    )
    stopWordsRemover = StopWordsRemover(
        inputCol="cleaned_tweet_words", outputCol="cleaned_tweet_nostop"
    )
    polarityCalc = polarityCalculator()
    countVectorizer = CountVectorizer(inputCol="cleaned_tweet_nostop", outputCol="cv")
    idf = IDF(inputCol="cv", outputCol="features")
    sentimentStringIdx = StringIndexer(inputCol="polarity", outputCol="label")
    logisticRegression = (
        LogisticRegression()
    )  # defaulted to featuresCol='features', labelCol='label'

    dataCleaningStages = [cleanTweet, regexTokenizer, stopWordsRemover]
    featureLabelMapStages = [countVectorizer, idf, sentimentStringIdx]

    return (
        Pipeline(
            stages=dataCleaningStages
            + [polarityCalc]
            + featureLabelMapStages
            + [logisticRegression]
        ),
        logisticRegression,
    )


def main(argv):
    # args is a list of the command line args
    cores = int(argv[0])
    percentage = int(argv[1])
    filename = "temp.csv"

    if len(argv) > 2:
        filename = argv[2]

    # print(f"partitions: {cores}, percentage: {percentage}")

    # loading dataset and preprocessing
    from pyspark.sql import SparkSession
    from src.utils.dataset import getPolarity
    from src.jobs.spark_etl import extract

    sparkSession = (
        SparkSession.builder.master(f"local[{cores}]")
        .appName(f"Global DT with {cores} partitions")
        .config("spark.driver.memory", "16g")
        .config("spark.executor.memory", "16g")
        .getOrCreate()
    )

    df = extract(sparkSession)

    polarity = sparkSession.udf.register("Polarity", lambda record: getPolarity(record))

    # training phase
    df_train, df_test = df.randomSplit([0.70, 0.30], seed=123456)
    df_train.cache()

    start = time.time()
    # MLlib code:

    pipeline, _ = pipelineCv()
    pipelineModel = pipeline.fit(df_train)

    end = time.time()
    print(f"Building phase took: {end - start} seconds")
    print(f"{end - start}")

    if len(argv) > 2:
        with open(filename, "a") as f:
            print(
                f"{cores},{percentage},{end - start}",
                file=f,
            )

    sparkSession.stop()


if __name__ == "__main__":
    main(sys.argv[1:])
