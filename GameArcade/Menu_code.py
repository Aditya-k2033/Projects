import tkinter as tk
import socket
import threading
from Server_riddle import server_game_riddle
from Client_riddle import client_game_riddle
from Script_riddle_client import Run_Script
from Script_riddle_server import Run_Script_server
import os

# Function to start the riddle game server


def riddle_server():
    server_game_riddle()


def riddle_client():
    Run_Script()


# Main menu window
def main_menu():
    root = tk.Tk()
    root.title("Game Menu")

    # Create buttons to start different games
    riddle_game_button_client = tk.Button(
        root, text="Start Riddle for player 1", command=Run_Script)
    riddle_game_button_client.pack()

    riddle_game_button_server = tk.Button(
        root, text="Start Riddle Server", command=Run_Script_server)
    riddle_game_button_server.pack()

    root.mainloop()


if __name__ == "__main__":
    main_menu()
