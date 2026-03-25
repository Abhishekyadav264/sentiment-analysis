import streamlit as St
from textblob import TextBlob


St.title("Sentiment Analysis App")
St.divider()

St.subheader("Enter your sentence to analyze its sentiment")
input_text = St.text_input("Enter your sentence:")
button = St.button("Check")

if input_text and button:
    blob = TextBlob(input_text)
    sentiment = blob.sentiment.polarity
    
    if sentiment > 0:
        St.success("Sentiment Positive")
    elif sentiment < 0:
        St.error("Sentiment Negative")
    else:
        St.info("Sentiment Natural")
        
    St.write(f"Sentiment Score: {sentiment : .2f}")
