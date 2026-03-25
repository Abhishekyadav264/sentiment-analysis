import streamlit as st
from textblob import TextBlob
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

st.title("Sentiment Analysis App")
st.divider()

st.subheader("Enter your sentence to analyze its sentiment")

input_text = st.text_input("Enter your sentence:")
button = st.button("Check")

if button:
    if input_text.strip() == "":
        st.warning("Please enter some text")
    else:
        blob = TextBlob(input_text)
        sentiment = blob.sentiment.polarity

        if sentiment > 0:
            st.success("Sentiment: Positive")
        elif sentiment < 0:
            st.error("Sentiment: Negative")
        else:
            st.info("Sentiment: Neutral")

        # st.write(f"Sentiment Score: {sentiment:.2f}")
        st.write(f"Sentiment Score: {int((sentiment) * 100)}")

