import tkinter as tk
from tkinter import ttk, messagebox
import random
import pygame

# Initialize pygame mixer and play background music
pygame.mixer.init()
pygame.mixer.music.load("Sleep Music 30 Minutes Lofi.mp3")
pygame.mixer.music.set_volume(0.08)  # 50% volume
pygame.mixer.music.play(-1)  # Loop indefinitely

correct_sound = pygame.mixer.Sound("kids-saying-yay-sound-effect_3.wav")
pygame.mixer.music.set_volume(0.2)  # 50% volume
incorrect_sound = pygame.mixer.Sound("extremely-loud-incorrect-buzzer_0cDaG20.wav")
pygame.mixer.music.set_volume(0.2)  # 50% volume

# Global variables
score = 0
question_count = 0
difficulty = None
first_attempt = True
num1 = num2 = operation = None

# Difficulty ranges
difficulty_ranges = {
    'Easy': (1, 9),
    'Moderate': (10, 99),
    'Advanced': (1000, 2000)
}

# Styling
custom_font = ("Times New Roman", 30)
bg_color = "#b6bfc7"
btn_color = "#4f7390"
btn_fg = "white"

# Exit fullscreen with Escape
def exit_fullscreen(event=None):
    root.attributes('-fullscreen', False)

# Initialize the main application window
root = tk.Tk()
root.title("Maths Quiz")
root.configure(bg=bg_color)
root.attributes('-fullscreen', True)
root.bind("<Escape>", exit_fullscreen)

# Function: displayMenu
def displayMenu():
    menu_frame.tkraise()

# Function: randomInt
def randomInt():
    min_val, max_val = difficulty_ranges[difficulty]
    return random.randint(min_val, max_val)

# Function: decideOperation
def decideOperation():
    return random.choice(['+', '-'])

# Function: displayProblem
def displayProblem():
    global num1, num2, operation, first_attempt
    first_attempt = True
    num1 = randomInt()
    num2 = randomInt()
    operation = decideOperation()
    question_label.config(text=f"{num1} {operation} {num2} = ")
    progress_label.config(text=f"Question {question_count + 1} of 10")
    answer_entry.delete(0, tk.END)
def isCorrect():
    global score, question_count, first_attempt
    try:
        user_answer = int(answer_entry.get())
        correct_answer = num1 + num2 if operation == '+' else num1 - num2
        if user_answer == correct_answer:
            correct_sound.play()
            score += 10 if first_attempt else 5
            question_count += 1
            if question_count < 10:
                displayProblem()
            else:
                displayResults()
        else:
            if first_attempt:
                first_attempt = False
                incorrect_sound.play()
                messagebox.showinfo("Try Again", "WRONG, try again")
                answer_entry.delete(0, tk.END)
            else:
                incorrect_sound.play()
                question_count += 1
                if question_count < 10:
                    displayProblem()
                else:
                    displayResults()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a number.")

# Function: displayResults
def displayResults():
    quiz_frame.pack_forget()
    result_frame.pack(fill="both", expand=True)
    result_label.config(text=f"Your score: {score}/100")
    rank = "A+" if score >= 90 else "A" if score >= 80 else "B" if score >= 70 else "C" if score >= 60 else "D"
    rank_label.config(text=f"Rank: {rank}")

# Function: startQuiz
def startQuiz(level):
    global difficulty, score, question_count
    difficulty = level
    score = 0
    question_count = 0
    result_frame.pack_forget()
    quiz_frame.pack(fill="both", expand=True)
    displayProblem()

# Function: playAgain
def playAgain():
    displayMenu()
    

# Hover effects
def on_enter(e):
    e.widget['background'] = '#5f9ea0'

def on_leave(e):
    e.widget['background'] = btn_color

# Exit fullscreen with Escape
def exit_fullscreen(event=None):
    root.attributes('-fullscreen', False)

# Menu Frame
menu_frame = tk.Frame(root, bg=bg_color)
menu_frame.pack(fill="both", expand=True)

# Configure grid weights for full expansion
menu_frame.grid_rowconfigure(1, weight=1)
for i in range(3):
    menu_frame.grid_columnconfigure(i, weight=1)

# Title label
ttk.Label(menu_frame, text="🧠 Select Difficulty Level", font=("Arial", 16)).grid(
    row=0, column=0, columnspan=3, pady=10
)

# Difficulty buttons
for i, level in enumerate(["Easy", "Moderate", "Advanced"]):
    btn = tk.Button(
        menu_frame,
        text=level,
        font=custom_font,
        bg=btn_color,
        fg=btn_fg,
        command=lambda l=level: startQuiz(l)
    )
    btn.grid(row=1, column=i, padx=10, pady=5, sticky="nsew")
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# Quiz Frame
quiz_frame = tk.Frame(root, bg=bg_color)

quiz_frame.grid_rowconfigure(0, weight=1)
quiz_frame.grid_rowconfigure(1, weight=1)
quiz_frame.grid_rowconfigure(2, weight=1)
quiz_frame.grid_columnconfigure(0, weight=1)

question_label = tk.Label(quiz_frame, text="", font=custom_font, bg=bg_color)
question_label.grid(row=0, column=0, pady=10, sticky="nsew")

progress_label = tk.Label(quiz_frame, text="", font=custom_font, bg=bg_color)
progress_label.grid(row=1, column=0, sticky="nsew")

answer_entry = ttk.Entry(quiz_frame, font=custom_font)
answer_entry.grid(row=2, column=0, pady=5, sticky="nsew")

submit_btn = tk.Button(quiz_frame, text="Submit", font=custom_font, bg=btn_color, fg=btn_fg, command=isCorrect)
submit_btn.grid(row=3, column=0, pady=5, sticky="nsew")
submit_btn.bind("<Enter>", on_enter)
submit_btn.bind("<Leave>", on_leave)

# Result Frame
result_frame = tk.Frame(root, bg=bg_color)

result_frame.grid_rowconfigure(0, weight=1)
result_frame.grid_rowconfigure(1, weight=1)
result_frame.grid_rowconfigure(2, weight=1)
result_frame.grid_rowconfigure(3, weight=1)
result_frame.grid_columnconfigure(0, weight=1)

result_label = tk.Label(result_frame, text="", font=custom_font, bg=bg_color)
result_label.grid(row=0, column=0, pady=10, sticky="nsew")

rank_label = tk.Label(result_frame, text="", font=custom_font, bg=bg_color)
rank_label.grid(row=1, column=0, sticky="nsew")

play_btn = tk.Button(result_frame, text="Play Again", font=custom_font, bg=btn_color, fg=btn_fg, command=playAgain)
play_btn.grid(row=2, column=0, pady=5, sticky="nsew")
play_btn.bind("<Enter>", on_enter)
play_btn.bind("<Leave>", on_leave)

exit_btn = tk.Button(result_frame, text="Exit", font=custom_font, bg=btn_color, fg=btn_fg, command=root.quit)
exit_btn.grid(row=3, column=0, pady=5, sticky="nsew")
exit_btn.bind("<Enter>", on_enter)
exit_btn.bind("<Leave>", on_leave)

# Start with menu
displayMenu()
root.mainloop()
