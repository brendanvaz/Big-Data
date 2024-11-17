import pyspark.sql.functions as sql_f
from pyspark.ml import Transformer
from pyspark.ml.feature import SQLTransformer
from pyspark.sql import DataFrame

import src.utils.constants as constants
from src.utils.text import clean_text


class CleanTweet(Transformer):
    def __init__(self):
        super(CleanTweet, self).__init__()

    def _transform(self, df: DataFrame) -> DataFrame:
        # drop NULLs
        df.dropna()
        df = df.na.drop(
            "any",
            subset=[
                "created_at",
                "tweet_id",
                "tweet",
                "likes",
                "retweet_count",
                "user_followers_count",
                "country",
                "candidate",
            ],
        )
        # majority of tweets are categorized into either `USA` or `United States of America`
        # therefore, we can filter out the rest as bad data
        df = df.where(
            "country LIKE 'United States' or country LIKE 'United States of America'"
        )
        df = df.drop(*["country", "continent"])
        # clean corrupt data
        df = df.where(df.user_join_date < "2022-05-05")
        # dropping non-relevant fields
        df = df.drop(*["user_name", "user_screen_name", "user_description"])
        # drop records that don't have at least 10 likes
        df = df.where(f"likes > {constants.TwitterData.MIN_N_O_LIKES.value}")
        # removal of URIs and Mentions
        return df.withColumn("cleaned_tweet", clean_text(sql_f.col("tweet")))


def polarityCalculator():
    return SQLTransformer(
        statement="SELECT tweet_id, created_at, tweet, likes, retweet_count"
        ",source, user_id, user_join_date, user_followers_count, user_location"
        ",lat, long, city, state, state_code, tweet, candidate, cleaned_tweet_nostop, polarity(cleaned_tweet_nostop) polarity"
        " FROM __THIS__"
    )
