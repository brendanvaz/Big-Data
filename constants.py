import os
from enum import Enum

from pyspark.sql.types import (
    DoubleType,
    FloatType,
    StringType,
    StructField,
    StructType,
    TimestampType,
)

import definitions

# Schema for Datasets
SCHEMA_DATASET = StructType(
    [
        StructField("created_at", TimestampType(), True),
        StructField("tweet_id", StringType(), True),
        StructField("tweet", StringType(), True),
        StructField("likes", FloatType(), True),
        StructField("retweet_count", FloatType(), True),
        StructField("source", StringType(), True),
        StructField("user_id", StringType(), True),
        StructField("user_name", StringType(), True),
        StructField("user_screen_name", StringType(), True),
        StructField("user_description", StringType(), True),
        StructField("user_join_date", TimestampType(), True),
        StructField("user_followers_count", FloatType(), True),
        StructField("user_location", StringType(), True),
        StructField("lat", DoubleType(), True),
        StructField("long", DoubleType(), True),
        StructField("city", StringType(), True),
        StructField("country", StringType(), True),
        StructField("continent", StringType(), True),
        StructField("state", StringType(), True),
        StructField("state_code", StringType(), True),
        StructField("collected_at", TimestampType(), True),
    ]
)


class Filepath(Enum):
    """
    Filepath enum
    """

    TRUMP_HASHTAG = os.path.join(
        definitions.ROOT_DIR, "data", "hashtag_donaldtrump.csv"
    )
    BIDEN_HASHTAG = os.path.join(definitions.ROOT_DIR, "data", "hashtag_joebiden.csv")
    VOTING = os.path.join(definitions.ROOT_DIR, "data", "voting.csv")
    ETL_OUTPUT = os.path.join(
        definitions.ROOT_DIR,
        "data",
        "output",
        "logisticRegression = LogisticRegression()  # defaulted to featuresCol='features', labelCol='label'etl_output.csv",
    )


class TwitterData(Enum):
    """
    Twitter data enum
    """

    MIN_N_O_LIKES = 10
