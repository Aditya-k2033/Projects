import tkinter as tk
import socket
import threading
import os

# Function to start the riddle game server

command4 = "python /Users/adityakhurana/Developer/CN_Proj/Menu_code.py"


def Play_riddle():
    os.system(
        f"osascript -e 'tell app \"Terminal\" to do script \"{command4}\"'")


def Play_TTT():
    print("Placeholder")


# Main menu window
def main_menu():
    root = tk.Tk()
    root.title("Choose a game")

    # Create buttons to start different games
    Game_button_riddle = tk.Button(
        root, text="Play Riddles", command=Play_riddle)
    Game_button_riddle.pack()

    Game_button_TTT = tk.Button(
        root, text="Play TicTacToe", command=Play_TTT)
    Game_button_TTT.pack()

    root.mainloop()


if __name__ == "__main__":
    main_menu()
