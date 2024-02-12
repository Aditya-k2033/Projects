import socket
import tkinter as tk
import subprocess


def client_game_riddle():

    def receive_riddle(sock):
        riddle = sock.recv(1024).decode()
        riddle_label.config(text=riddle)

    def send_answer():
        answer = answer_entry.get()
        answer_entry.delete(0, tk.END)  # Clear the entry field
        client_socket.send(answer.encode())
        feedback = client_socket.recv(1024).decode()
        feedback_label.config(text=feedback)

    # Create a Tkinter window
    root = tk.Tk()
    root.title("Riddle Game")

    # # Create GUI elements
    riddle_label = tk.Label(
        root, text="Riddle will appear here", wraplength=300)
    riddle_label.pack()

    answer_entry = tk.Entry(root)
    answer_entry.pack()

    submit_button = tk.Button(root, text="Submit Answer", command=send_answer)
    submit_button.pack()

    feedback_label = tk.Label(root, text="", fg="green")
    feedback_label.pack()

    # # Create a socket for the client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 32007))

    # Receive and display the first riddle
    receive_riddle(client_socket)

    # Run the Tkinter main loop
    root.mainloop()


if __name__ == "__main__":
    client_game_riddle()
