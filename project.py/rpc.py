import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]
results = {
    ("Rock", "Scissors"): "You Win! 🎉",
    ("Paper", "Rock"): "You Win! 🎉",
    ("Scissors", "Paper"): "You Win! 🎉",
    ("Scissors", "Rock"): "You Lose 😞",
    ("Rock", "Paper"): "You Lose 😞",
    ("Paper", "Scissors"): "You Lose 😞",
}

player_score = 0
comp_score = 0

def play(player_choice):
    global player_score, comp_score
    computer_choice = random.choice(choices)

    # Start animation
    animate_result("🤔", lambda: show_result(player_choice, computer_choice))

def show_result(player, computer):
    global player_score, comp_score

    if player == computer:
        result = "It's a Draw 🤝"
    else:
        result = results.get((player, computer), "You Lose 😞")

    # Update score
    if "Win" in result:
        player_score += 1
    elif "Lose" in result:
        comp_score += 1

    result_label.config(text=f"{player} vs {computer}\n{result}")
    score_label.config(text=f"👤 You: {player_score}   🤖 Computer: {comp_score}")

def animate_result(text, after_animation):
    # Flicker animation effect
    flashes = ["🪨", "📄", "✂️", "", "🪨", "📄", "✂️", "", ""]

    def step(i=0):
        if i < len(flashes):
            result_label.config(text=flashes[i])
            root.after(100, lambda: step(i + 1))
        else:
            after_animation()

    step()

# UI setup
root = tk.Tk()
root.title("Rock Paper Scissors 🎮")
root.geometry("400x350")
root.resizable(False, False)

title = tk.Label(root, text="Rock Paper Scissors", font=("Helvetica", 20, "bold"))
title.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

for choice in choices:
    tk.Button(
        button_frame,
        text=choice,
        font=("Helvetica", 14),
        width=10,
        command=lambda c=choice: play(c)
    ).pack(side=tk.LEFT, padx=10)

result_label = tk.Label(root, text="", font=("Helvetica", 16), pady=20)
result_label.pack()

score_label = tk.Label(root, text="👤 You: 0   🤖 Computer: 0", font=("Helvetica", 14))
score_label.pack()

root.mainloop()
