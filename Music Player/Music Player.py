import pygame
import os
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Music Player")
        self.master.geometry("400x600")

        # Load the background image
        image_file = "pic1.jpg"
        image = Image.open(image_file)
        photo = ImageTk.PhotoImage(image)

        # Create a label with the image as the background
        self.background_label = Label(self.master, image=photo)
        self.background_label.image = photo
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        # Load the logo image and resize it
        logo_file = "bts1.jpg"
        logo_image = Image.open(logo_file)
        logo_image = logo_image.resize((70, 70), Image.ANTIALIAS)
        logo_photo = ImageTk.PhotoImage(logo_image)

        # Create a label with the logo image
        self.logo_label = Label(self.master, image=logo_photo, bg="white")
        self.logo_label.image = logo_photo
        self.logo_label.place(x=600, y=120)
        # Create the other widgets and position them on top of the background label
        self.song_label = Label(self.background_label, text="songs", bg="white")
        self.song_label.place(relx=0.5, rely=0.2, anchor=CENTER)

        self.select_button = Button(self.background_label, text="Select Song", command=self.select_song, bg="purple", fg="white", font=("aharoni", 14))
        self.select_button.place(relx=0.5, rely=0.4, anchor=CENTER)

        self.play_button = Button(self.background_label, text="Play", command=self.play_song, bg="orange", fg="white", font=("aharoni", 16))
        self.play_button.place(relx=0.5, rely=0.6, anchor=CENTER)

        self.stop_button = Button(self.background_label, text="Stop", command=self.stop_song, bg="green", fg="white", font=("aharoni", 14))
        self.stop_button.place(relx=0.5, rely=0.7, anchor=CENTER)

        self.song_path = ""

        pygame.init()

    def select_song(self):
        initial_dir = "/"
        self.song_path = filedialog.askopenfilename(initialdir=initial_dir, filetypes=[("Audio Files", "*.mp3;*.wav")])
        if self.song_path != "":
            self.song_label["text"] = self.song_path

    def play_song(self):
        if self.song_path != "":
            pygame.mixer.music.load(self.song_path)
            pygame.mixer.music.play()

    def stop_song(self):
        pygame.mixer.music.stop()

if __name__ == '__main__':
    root = Tk()
    MusicPlayer(root)
    root.mainloop()
