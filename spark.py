from pyspark.sql import SparkSession


def initSparkSession(master="local", appName="PySparkApp"):
    return SparkSession.builder.master(master).appName(appName).getOrCreate()
