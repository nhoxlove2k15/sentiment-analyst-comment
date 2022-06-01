from transformers import pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

def predict_comment(text_input):
    return sentiment_pipeline(text_input)
