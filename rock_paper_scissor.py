import tkinter as tk
from tkinter import messagebox
import random
import pygame  
pygame.mixer.init()

win_sound = pygame.mixer.Sound("nxtlvl.wav")
lose_sound = pygame.mixer.Sound("go.wav")
draw_sound = pygame.mixer.Sound("draw.wav")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        pygame.mixer.Sound.play(draw_sound)  
        return 'It\'s a tie!'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        pygame.mixer.Sound.play(win_sound)  
        return 'You win!'
    else:
        pygame.mixer.Sound.play(lose_sound)  
        return 'Otto wins!'

def play_game():
    player_input = choice_entry.get().strip().lower()
    if player_input == 'r':
        player_choice = 'rock'
    elif player_input == 'p':
        player_choice = 'paper'
    elif player_input == 's':
        player_choice = 'scissors'
    elif player_input in ['rock', 'paper', 'scissors']:
        player_choice = player_input
    else:
        messagebox.showerror("Invalid Input", "Please enter 'rock', 'paper', 'scissors', 'r', 'p', or 's'.")
        return

    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)
    result_label.config(text=f"You chose: {player_choice.capitalize()}\nOtto chose: {computer_choice.capitalize()}\n{result}")

    if result == 'You win!':
        scores['player'] += 1
    elif result == 'Otto wins!':
        scores['otto'] += 1
    else:
        scores['draw'] += 1

    update_score_label()

def update_score_label():
    score_label.config(text=f"Score\nYou: {scores['player']}  Otto: {scores['otto']}  Draws: {scores['draw']}")

def start_game(event=None):
    player_name = name_entry.get()
    if not player_name:
        messagebox.showerror("Name Error", "Please enter your name.")
        return

    name_label.config(text=f"{player_name}'s Turn")
    play_button.config(state=tk.NORMAL)

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x600")

content_frame = tk.Frame(root, bg='#8FCDEF')
content_frame.place(relwidth=1, relheight=1)

name_label = tk.Label(content_frame, text="Enter your name:", bg='#8FCDEF', font=("Helvetica", 16, "bold"))
name_label.pack(pady=10)

name_entry = tk.Entry(content_frame, font=("Helvetica", 14))
name_entry.pack(pady=5)

start_button = tk.Button(content_frame, text="Start Game", command=start_game, font=("Helvetica", 14, "bold"), bg='#1E90FF', fg='white')
start_button.pack(pady=10)

choice_label = tk.Label(content_frame, text="Enter your choice (rock/paper/scissors or r/p/s):", bg='#8FCDEF', font=("Helvetica", 14, "bold"))
choice_label.pack(pady=10)

choice_entry = tk.Entry(content_frame, font=("Helvetica", 14))
choice_entry.pack(pady=5)

button_frame = tk.Frame(content_frame, bg='#8FCDEF')
button_frame.pack(pady=10)

def create_choice_block(text, color):
    block = tk.Label(button_frame, text=text, font=("Helvetica", 14, "bold"), bg=color, fg="white", relief="raised", padx=10, pady=10, width=15)
    block.grid(padx=10, pady=5)
    return block

rock_block = create_choice_block("✊ Rock (r)", "#f21f18")  # Red
paper_block = create_choice_block("✋ Paper (p)", "#28e036")  # Green
scissors_block = create_choice_block("✌️ Scissors (s)", "#901dcc")  # Blue

play_button = tk.Button(content_frame, text="Play", command=play_game, state=tk.DISABLED, font=("Helvetica", 14, "bold"), bg='#1E90FF', fg='white')
play_button.pack(pady=10)

result_label = tk.Label(content_frame, text="", bg='#8FCDEF', font=("Helvetica", 14, "bold"))
result_label.pack(pady=20)

score_label = tk.Label(content_frame, text="Score\nYou: 0  Otto: 0  Draws: 0", bg='#8FCDEF', font=("Helvetica", 14, "bold"))
score_label.pack(pady=10)

scores = {'player': 0, 'otto': 0, 'draw': 0}

root.bind('<Return>', start_game)

root.mainloop()

pygame.mixer.quit()
