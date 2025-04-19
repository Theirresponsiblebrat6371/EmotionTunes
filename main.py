from textblob import TextBlob
import random
import os
import pygame


def detect_emotion_and_genre(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity  


    if polarity >= 0.5:
      emotion = random.choice(["Very Happy", "Motivational"])
    elif polarity > 0 and polarity <= 0.5:
      emotion = "Happy"
    elif -0.2 <= polarity <= 0.2:
      emotion = "Neutral"
    elif polarity < 0 and polarity >= -0.5:
      emotion = "Sad"
    else:
      emotion = "Very Sad / Angry"  

    
    emotion_genre_map = {
      "Very Happy" : ["Pop", "EDM"],
      "Happy" : ["Pop"],
      "Sad" : ["Lo-fi"],
      "Neutral" : ["Romantic", "indie"],
      "Angry/Very Sad" : ["Metal", "Rock", "Phonk"],
      "Motivational" : ["Phonk"]
    }


    genres = emotion_genre_map.get(emotion, ["Indie"])
    selected_genre = random.choice(genres)
    print("Polarity score:", polarity)  
    return emotion, selected_genre



def Play_song_from_genre(genre):

    base_path = "songs" 
    genre_path = os.path.join(base_path, genre)


    print(f"Looking in: {genre_path}")


    if not os.path.exists(genre_path):
      print(f"No songs found for genre : {genre}")
      return   


    print("Files inside genre folder:", os.listdir(genre_path)) 


    songs = [song for song in os.listdir(genre_path) if song.endswith(".mp3") or song.endswith(".mpeg")]


    print("Filtered mp3 songs:", songs)


    if not songs:
      print(f"No mp3 file found in {genre_path}")
      return
    

    selected_song = random.choice(songs)
    song_path = os.path.join(genre_path,selected_song)

    print(f"🎵 Playing: {selected_song}")

    pygame.mixer.init()
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()

    return selected_song