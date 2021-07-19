import sys
import os

user = os.getlogin()
relative_path = f"C://Users//{user}//tictactoe//builder.py"

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('')

    return os.path.join(base_path, relative_path)