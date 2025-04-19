# EmotionTunes🎧🧠

An AI-powered desktop application that detects emotions in user-input text and recommends local songs that match the mood.

---

## 🔍 Features

- 🧠 Detects emotions using TextBlob sentiment analysis
- 🎵 Plays local music based on the detected emotion
- 💻 Simple GUI using Tkinter
- ⚡ Lightweight and works offline

---

## 📌 Emotions Detected

- 😊 Happy
- 😢 Sad
- 😠 Angry
- 😐 Neutral

> Each emotion is mapped to 1-2 local songs from the user's personal music collection.

---

## 🖥️ Tech Stack

- Python  
- Tkinter (GUI)  
- TextBlob (NLP)  
- `os` module for local audio playback  

---

## 🚀 How to Run

# Clone the repo
git clone https://github.com/yourusername/emotiontunes.git
cd emotiontunes

# Install dependencies
pip install textblob
python -m textblob.download_corpora

# Run the app
python app.py
