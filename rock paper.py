import tkinter as tk
from tkinter import Toplevel
from PIL import Image, ImageTk
import random

# Create the main window
root = tk.Tk()
root.title("Game Rock and Scissors")
root.geometry("500x400")
root.configure(bg="white")

# Define the choices and outcomes
choices = ["Rock", "Paper", "Scissors"]

# Load the images
rock_img = ImageTk.PhotoImage(Image.open("rock.png").resize((100, 100)))
paper_img = ImageTk.PhotoImage(Image.open("paper.png").resize((100, 100)))
scissors_img = ImageTk.PhotoImage(Image.open("scissors.png").resize((100, 100)))


# Function to create the result window
def show_result(user_choice, computer_choice, result):
    # Create a new window for the result
    result_window = Toplevel(root)
    result_window.title("Result")
    result_window.geometry("300x300")
    result_window.configure(bg="pink")

    # Display user and computer choices
    user_label = tk.Label(result_window, text=f"Your choice: {user_choice}", font=("Arial", 12), bg="lightgreen")
    user_label.pack(pady=10)

    computer_label = tk.Label(result_window, text=f"Computer's choice: {computer_choice}", font=("Arial", 12),
                              bg="lightgreen")
    computer_label.pack(pady=10)

    result_label = tk.Label(result_window, text=result, font=("Arial", 16, "bold"), bg="lightgreen", fg="blue")
    result_label.pack(pady=20)

    # Close the result window after 5 seconds
    result_window.after(5000, result_window.destroy)


# Function to determine the winner
def determine_winner(user_choice):
    computer_choice = random.choice(choices)
    result = ""

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
            (user_choice == "Scissors" and computer_choice == "Paper") or \
            (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    # Show the result in a new window
    show_result(user_choice, computer_choice, result)


# Create a label at the top with a title
title_label = tk.Label(root, text="Rock, Paper, Scissors Game", bg="black", fg="white",
                       font=("Arial", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=3, pady=10)

# Create buttons with images and commands for user input
rock_button = tk.Button(root, image=rock_img, command=lambda: determine_winner("Rock"))
rock_button.grid(row=1, column=0, padx=10, pady=10)

paper_button = tk.Button(root, image=paper_img, command=lambda: determine_winner("Paper"))
paper_button.grid(row=1, column=1, padx=10, pady=10)

scissors_button = tk.Button(root, image=scissors_img, command=lambda: determine_winner("Scissors"))
scissors_button.grid(row=1, column=2, padx=10, pady=10)

# Add labels under each button (Rock, Paper, Scissors)
rock_label = tk.Label(root, text="Rock", font=("Arial", 12), bg="blue", fg="white")
rock_label.grid(row=2, column=0)

paper_label = tk.Label(root, text="Paper", font=("Arial", 12), bg="black", fg="white")
paper_label.grid(row=2, column=1)

scissors_label = tk.Label(root, text="Scissors", font=("Arial", 12), bg="black", fg="white")
scissors_label.grid(row=2, column=2)

# Center the content in the window by using column weights
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Run the main loop
root.mainloop()
