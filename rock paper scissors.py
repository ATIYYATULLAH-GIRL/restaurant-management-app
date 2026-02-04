import tkinter as tk
from tkinter import messagebox
import random

CHOICES = ["Rock", "Paper", "Scissors"]

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return "You Win!"
    else:
        return "Computer Wins!"

def play(choice):
    global user_score, computer_score

    computer_choice = random.choice(CHOICES)
    result = determine_winner(choice, computer_choice)

    result_label.config(text=f"Your Choice: {choice}\nComputer's Choice: {computer_choice}\n{result}")

    if "You Win" in result:
        user_score += 1
    elif "Computer Wins" in result:
        computer_score += 1

    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text="Score - You: 0 | Computer: 0")
    result_label.config(text="Make your move!")

user_score = 0
computer_score = 0

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")
root.resizable(False, False)

title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

result_label = tk.Label(root, text="Make your move!", font=("Arial", 12))
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

reset_btn = tk.Button(root, text="Reset Game", command=reset_game)
reset_btn.pack(pady=10)

exit_btn = tk.Button(root, text="Exit", command=root.destroy)
exit_btn.pack()

root.mainloop()