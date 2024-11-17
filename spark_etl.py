import pyspark.sql.functions as sql_f

import src.utils.constants as constants
from src.utils.spark import initSparkSession
from src.utils.text import clean_text


def extract(sparkSession):
    df_trump = (
        sparkSession.read.option("wholeFile", "true")
        .option("multiline", "true")
        .schema(constants.SCHEMA_DATASET)
        .csv(constants.Filepath.TRUMP_HASHTAG.value, header=True)
    ).withColumn("candidate", sql_f.lit("TRUMP"))

    df_biden = (
        sparkSession.read.option("wholeFile", "true")
        .option("multiline", "true")
        .schema(constants.SCHEMA_DATASET)
        .csv(constants.Filepath.BIDEN_HASHTAG.value, header=True)
    ).withColumn("candidate", sql_f.lit("BIDEN"))

    return df_trump.union(df_biden)


def transform(input_df):
    df = input_df.na.drop(  # drop NULLs
        "all",
        subset=[
            "tweet",
            "likes",
            "retweet_count",
            "user_followers_count",
            "country",
            "candidate",
        ],
    )
    df = (
        df.where(  # drop records that are not tweets from the US
            "country LIKE 'United States' or country LIKE 'United States of America'"
        )
        .drop(
            *[
                "country",
                "continent",
                "tweet_id",
                "user_name",
                "user_screen_name",
                "user_description",
            ]
        )  # dropping non-relevant fields
        .where("likes > 10")  # drop records that don't have at least 10 likes
        .withColumn("cleaned_tweet", clean_text(sql_f.col("tweet")))
    )

    return df


def main():
    #  Spark Session for ETL job
    sparkETLSession = initSparkSession(appName="SentimentAnalysisJob")
    #  Extract data from CSV
    df = extract(sparkETLSession)
    #  Cache before applying transformations
    df.cache()
    #  Apply transformations on cached DataFrame
    df = transform(df)
    #  Write transformed data to parquet
    df.write(
        format="parquet", mode="overwrite", path=constants.Filepath.ETL_OUTPUT.value
    )
    #  Stop underlying SparkContext
    sparkETLSession.stop()


if __name__ == "__main__":
    main()
