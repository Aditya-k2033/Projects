import os


def Run_Script_server():
    command3 = "python /Users/adityakhurana/Developer/CN_Proj/Server_riddle.py"

    os.system(
        f"osascript -e 'tell app \"Terminal\" to do script \"{command3}\"'")


if __name__ == "__main__":
    Run_Script_server()
