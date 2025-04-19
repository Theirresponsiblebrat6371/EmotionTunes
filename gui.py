import tkinter as tk
from tkinter import messagebox
from main import Play_song_from_genre, detect_emotion_and_genre
import pygame

current_emotion = None
current_genre = None

root = tk.Tk()
root.title("Emotion Music Player")
root.geometry("400x300")



def onsubmit():
    global current_emotion, current_genre
    mood = entry.get()
    if not mood.strip():
        messagebox.showerror("Input Error", "Please enter a mood.")
        return
    current_emotion, current_genre = detect_emotion_and_genre(mood)
    emotion_label.config(text=f"Detected Emotion: {current_emotion}")
    genre_label.config(text=f"Suggested Genre: {current_genre}")

    selected_song = Play_song_from_genre(current_genre)
    song_label.config(text=f"Song Playing: {selected_song}")


is_paused = False

def toggle_play_pause():
    global is_paused
    if is_paused:
        pygame.mixer.music.unpause()
        play_pause_button.config(text="Pause ⏸️")
        is_paused = False
    else:
        pygame.mixer.music.pause()
        play_pause_button.config(text="Play ▶️")
        is_paused = True




def stop():
    pygame.mixer.music.stop()
def pause():
    pygame.mixer.music.pause()
def resume():   
    pygame.mixer.music.unpause()


title = tk.Label(root, text="Emotion Music Player", font=("Helvetica", 16))
title.pack(pady=10)

entry_label = tk.Label(root, text="How are you feeling today?")
entry_label.pack()

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

entry.bind("<Return>", lambda event: onsubmit())



result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=5)

emotion_label = tk.Label(root, text="Detected Emotion: ", font=("Helvetica", 12))
emotion_label.pack()

genre_label = tk.Label(root, text="Suggested Genre: ", font=("Helvetica", 12))
genre_label.pack()

song_label = tk.Label(root, text="Song Playing: ", font=("Helvetica", 12))
song_label.pack()




submit_button = tk.Button(root, text="Submit", command=onsubmit)
submit_button.pack(pady=10)

controls_frame = tk.Frame(root)
controls_frame.pack(pady=10)

play_pause_button = tk.Button(controls_frame, text="Pause ⏸️", command=toggle_play_pause)
play_pause_button.pack(side=tk.LEFT, padx=5)

stop_button = tk.Button(controls_frame, text="Stop", command=stop)
stop_button.pack(side=tk.LEFT, padx=5)




root.mainloop()