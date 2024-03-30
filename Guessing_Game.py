import random
import tkinter as tk

# Define the data (same as before)
data = {
    "Ape": -1,
    "Grape": -1,
    "sylvy": -1,
    "pilvy": -1,
    "WoW": 5,
}

# Function to generate a random value and points
def get_random_value_and_points():
    random_value = random.choice(list(data.keys()))
    points = data[random_value]
    return random_value, points

# Function to start the game
def start_game():
    global player_name, current_chance, result_text

    # Get player name from the input field
    player_name = player_name_entry.get()

    # Reset chance and result
    current_chance = 1
    result_text.set("")

    # Enable the "Next Chance" button
    next_chance_button.config(state="normal")

    # Display initial message
    result_text.set(f"Hi {player_name}, get ready for the fruit frenzy!")

# Function to handle button click
def next_chance():
    global current_chance

    # Check if remaining chances
    if current_chance == 4:  # Check if current chance is 3 (corrected)
        next_chance_button.config(state="disabled")
        result_text.set(f"Thanks for playing, {player_name}!")
        return

    # Generate random value and points
    random_value, points = get_random_value_and_points()

    # Update result text with current chance and earned points
    result_text.set(f"Hi {player_name}, chance {current_chance}/3: You got {random_value}! You earned {points} points.")

    current_chance += 1

# Initialize Tkinter window
window = tk.Tk()
window.title("Fruit Point Game")

# Set window size
window.geometry("400x600")
# Player name entry
player_name_label = tk.Label(window, text="Enter your name:")
player_name_label.place(relx=0.5, rely=0.36, anchor="center")

player_name_entry = tk.Entry(window)
player_name_entry.place(relx=0.5, rely=0.4, anchor="center")

# Start game button
start_game_button = tk.Button(window, text="Start Game", command=start_game)
start_game_button.place(relx=0.5, rely=0.46, anchor="center")

# Result text
result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text)
result_label.place(relx=0.5, rely=0.5, anchor="center")

# Next chance button
next_chance_button = tk.Button(window, text="Next Chance", command=next_chance, state="disabled")
next_chance_button.place(relx=0.5, rely=0.55, anchor="center")

window.mainloop()
