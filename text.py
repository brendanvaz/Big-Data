import pyspark.sql.functions as sql_f


def clean_text(col):
    col = sql_f.regexp_replace(
        col,
        "(?:(https?|ircs?):\\/\\/(?:www\\.)?|www\\.)((?:(?:[-\\w]+\\.)+)[-\\w]+)(?::\\d+)?(?:\\/((?:["
        "-a-zA-Z;./\\d#:_?=&,]*)))?",
        "",
    )  # Remove URIs
    col = sql_f.regexp_replace(col, "@(.+?)(?:\\s|$)", "")  # Remove mentions
    return col
