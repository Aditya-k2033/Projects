import socket


def server_game_riddle():
    # Create a socket for the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 32007))
    server_socket.listen(2)

    print("Waiting for players...")

    # Accept two player connections
    player1_socket, player1_address = server_socket.accept()
    print(f"Player 1 connected: {player1_address}")
    player2_socket, player2_address = server_socket.accept()
    print(f"Player 2 connected: {player2_address}")

    # Riddles
    riddles = [
        ("What has keys but can't open locks?", "A piano"),
        ("What has a head and a tail, but no body?", "A coin"),
        # Add more riddles here
    ]

    def send_riddle(player_socket, riddle):
        player_socket.send(f"Riddle: {riddle[0]}".encode())

    def evaluate_answer(answer, correct_answer):
        return answer.strip().lower() == correct_answer.lower()

    # Send riddles alternately to players
    for idx, riddle in enumerate(riddles):
        if idx % 2 == 0:
            send_riddle(player1_socket, riddle)
            player1_answer = player1_socket.recv(1024).decode()
            if evaluate_answer(player1_answer, riddle[1]):
                player1_socket.send("Correct!".encode())
            else:
                player1_socket.send("Wrong!".encode())

        else:
            send_riddle(player2_socket, riddle)
            player2_answer = player2_socket.recv(1024).decode()
            if evaluate_answer(player2_answer, riddle[1]):
                player2_socket.send("Correct!".encode())
            else:
                player2_socket.send("Wrong!".encode())

    # Close connections
    player1_socket.close()
    player2_socket.close()
    server_socket.close()


if __name__ == "__main__":
    server_game_riddle()
