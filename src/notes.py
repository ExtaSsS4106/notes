import eel
import sqlite3


class funcs:
    # Подключение к базе данных SQLite
    def db_start():
        global conn, cur
        conn = sqlite3.connect('notes.db')
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS notes (
                        id INTEGER PRIMARY KEY, 
                        note TEXT, 
                        text TEXT)""")
        conn.commit()
        print("База данных успешно инициализирована.")

    # Функция для добавления заметки
    @eel.expose
    def add_note(note, text=""):
        cur.execute("INSERT INTO notes (note, text) VALUES (?, ?)", (note, text))
        conn.commit()
        print(f"Заметка '{note}' добавлена.")


    # Функция для получения всех заметок с их ID
    @eel.expose
    def get_notes():
        cur.execute("SELECT id, note FROM notes")
        notes = cur.fetchall()
        print(f"Заметки загружены: {notes}")
        return [{'id': note[0], 'note': note[1]} for note in notes]


    # Функция для удаления заметки по ID
    @eel.expose
    def delete_note(note_id):
        cur.execute("DELETE FROM notes WHERE id=?", (note_id,))
        conn.commit()
        print(f"Заметка с ID {note_id} удалена.")


    # Функция для получения полного текста заметки по ID
    @eel.expose
    def get_note_text(note_id):
        cur.execute("SELECT text FROM notes WHERE id=?", (note_id,))
        result = cur.fetchone()
        return result[0]

    # Функция для обновления текста заметки
    @eel.expose
    def update_note_text(note_id, new_text):
        cur.execute("UPDATE notes SET text=? WHERE id=?", (new_text, note_id))
        conn.commit()
        print(f"Заметка с ID {note_id} обновлена.")


    # Закрытие соединения с базой данных
    def close_db():
        conn.close()
        print("Соединение с базой данных закрыто.")





    # Закрытие базы данных при завершении приложения
    @eel.expose
    def on_close():
        print("Закрытие приложения...")
        funcs.close_db()
        exit()


