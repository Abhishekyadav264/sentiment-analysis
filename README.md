# 🎯 Sentiment Analysis App
![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-ff4b4b?logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Language-Python-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Live-success)
![License](https://img.shields.io/badge/License-MIT-green)


A simple and interactive **Sentiment Analysis Web App** built using **Python** and **Streamlit**. This application allows users to input any sentence and instantly analyze whether the sentiment is **Positive, Negative, or Neutral**, along with a sentiment score.

🔗 **Live App:** https://emotion-analytics.streamlit.app/

---

## 🚀 Features

- 🔍 Real-time sentiment analysis
- 😊 Classifies text into:
  - Positive
  - Negative
  - Neutral
- 📊 Displays sentiment score (0–100 scale)
- ⚡ Fast and lightweight interface
- 🌐 User-friendly web UI built with Streamlit
- 🧠 Powered by Natural Language Processing (NLP)

---

## 💡 Use Cases

- 📱 Analyze social media comments and posts
- 🛍️ Understand customer feedback and reviews
- 📊 Perform basic sentiment-based data analysis
- 🎓 Educational project for NLP beginners
- 💬 Evaluate opinions in text data

---

## 🛠️ Tools & Technologies

- **Python** – Core programming language  
- **Streamlit** – Web app framework for UI  
- **TextBlob** – Sentiment analysis engine  
- **NLTK** – Natural Language Processing toolkit :contentReference[oaicite:0]{index=0}  

---

## ⚙️ How It Works

1. User enters a sentence in the input box  
2. The app processes the text using NLP techniques  
3. Sentiment polarity is calculated using TextBlob  
4. Output is displayed as:
   - Sentiment category (Positive/Negative/Neutral)
   - Sentiment score  

---
## 📂 Project Structure
```
Sentiment-Analysis-App
│── app.py
│── requirements.txt
```


## 📌 Conclusion

This project demonstrates how Natural Language Processing can be used to extract insights from text data in a simple and effective way. It serves as a strong foundation for building advanced text analytics and AI-based applications.

## 👤 Author

**Abhishek**  
Aspiring Data Analyst 


- `app.py` → Main Streamlit application file :contentReference[oaicite:1]{index=1}  
- `requirements.txt` → Dependencies list  

---

## ▶️ How to Run Locally

```bash
# Clone the repository
git clone https://github.com/your-username/sentiment-analysis-app.git

# Navigate to project folder
cd sentiment-analysis-app

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
