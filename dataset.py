from textblob import TextBlob


def getPolarity(textArray):
    """
    Returns the polarity of the textArray
    """
    score = TextBlob(" ".join(textArray)).sentiment.polarity
    if score < 0:
        return "Negative"
    if score == 0:
        return "Neutral"
    if score > 0:
        return "Positive"
