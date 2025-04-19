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
git clone https://github.com/Theirresponsiblebrat6371/EmotionTunes.git
cd emotiontunes

# Install dependencies
pip install textblob
python -m textblob.download_corpora

# Run the app
python app.py


---


🧠 How It Works
User enters a sentence in the text box

TextBlob analyzes the sentiment polarity:

Polarity > 0.1 → Happy

Polarity < -0.1 → Sad

Polarity ~0 → Neutral

A random song from the corresponding emotion folder is played


---


🧰 To-Do / Future Enhancements
Use a more advanced emotion classifier (e.g., BERT-based)

Add dynamic Spotify/Youtube integration

Add playlist view and pause/play control

Build a web version using Flask


---


👤 Author
Priyanshu Das
B.Tech – CSE (AI & ML)
📧 theirresponsiblebrat508@gmail.com
🎓 Rungta College of Engineering and Technology
