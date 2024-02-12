import os


def Run_Script():
    command2 = "python /Users/adityakhurana/Developer/CN_Proj/Client_riddle.py"

    os.system(
        f"osascript -e 'tell app \"Terminal\" to do script \"{command2}\"'")


if __name__ == "__main__":
    Run_Script()
