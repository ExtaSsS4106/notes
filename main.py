import eel
from src.notes import funcs

eel.init("web")

if __name__ == "__main__":
    funcs.db_start()
    eel.start("index.html", size=(935, 705), block=False)
    while True:
        eel.sleep(10)
