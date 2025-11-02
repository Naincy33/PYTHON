import tkinter as tk
from tkinter import PhotoImage
import random
import os
import requests

# ✅ Function to fetch online words
def get_online_words(count=10):
    try:
        words = []
        while len(words) < count:
            res = requests.get(f"https://random-word-api.herokuapp.com/word?number=1")
            if res.status_code == 200:
                word = res.json()[0]
                if word.isalpha() and len(word) >= 4:
                    words.append(word.lower())
        return words
    except:
        print("⚠️ Internet not available. Using default words.")
        return ['banana', 'rocket', 'wizard', 'castle', 'jungle', 'python', 'freedom', 'umbrella', 'glasses', 'sunshine']

# ✅ First batch of words
WORDS = get_online_words()

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game with Images")

        # 🖼 Load images hangman0.png to hangman6.png
        self.images = [PhotoImage(file=f"hangman{i}.png") for i in range(7)]
        self.word = random.choice(WORDS)
        self.missed = []
        self.correct = []

        self.setup_gui()

    def setup_gui(self):
        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady=10)

        self.word_label = tk.Label(self.root, text="_ " * len(self.word), font=("Arial", 24))
        self.word_label.pack(pady=10)

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack()

        self.letter_buttons = {}
        for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            btn = tk.Button(self.buttons_frame, text=letter, width=4, command=lambda l=letter: self.guess_letter(l.lower()))
            btn.grid(row=i // 9, column=i % 9)
            self.letter_buttons[letter] = btn

        self.status_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.status_label.pack(pady=10)

        self.reset_button = tk.Button(self.root, text="Play Again", command=self.reset_game)
        self.reset_button.pack(pady=10)
        self.reset_button.pack_forget()

        self.update_display()

    def update_display(self):
        self.image_label.config(image=self.images[len(self.missed)])
        display = " ".join([l if l in self.correct else "_" for l in self.word])
        self.word_label.config(text=display)

    def guess_letter(self, letter):
        self.letter_buttons[letter.upper()]["state"] = "disabled"

        if letter in self.word:
            self.correct.append(letter)
        else:
            self.missed.append(letter)

        self.update_display()
        self.check_game_over()

    def check_game_over(self):
        if all(l in self.correct for l in self.word):
            self.status_label.config(text=f"You won! Word was '{self.word}'")
            self.disable_all_buttons()
        elif len(self.missed) == 6:
            self.status_label.config(text=f"You lost! Word was '{self.word}'")
            self.disable_all_buttons()

    def disable_all_buttons(self):
        for btn in self.letter_buttons.values():
            btn["state"] = "disabled"
        self.reset_button.pack()

    def reset_game(self):
        new_words = get_online_words()
        self.word = random.choice(new_words)
        self.missed.clear()
        self.correct.clear()
        self.status_label.config(text="")
        self.reset_button.pack_forget()
        for btn in self.letter_buttons.values():
            btn["state"] = "normal"
        self.update_display()

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()


