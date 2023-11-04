import click
from Note import Note
from NoteApp import NoteApp
from datetime import datetime

class Main:
    def __init__(self):
        self.app = NoteApp()

    def run(self):
        self.app.load_notes_from_file()
        self.print_menu()
        while True:
            choice = input("Введите команду: ")
            if choice == "add":
                self.add_note()
            elif choice == "list":
                self.list_notes()
            elif choice == "update":
                self.update_note()
            elif choice == "delete":
                self.delete_note()
            elif choice == "filter":
                self.filter_notes_by_date()
            elif choice == "exit":
                self.app.save_notes_to_file()
                print("Программа завершена.")
                break
            else:
                print("Неизвестная команда. Попробуйте еще раз.")

    def add_note(self):
        title = input("Введите заголовок заметки: ")
        body = input("Введите тело заметки: ")
        self.app.add(title, body)
        print("Заметка успешно добавлена.")

    def list_notes(self):
        self.app.list_notes()

    def update_note(self):
        note_id = int(input("Введите ID заметки для обновления: "))
        title = input("Введите новый заголовок: ")
        body = input("Введите новое тело: ")
        self.app.update(note_id, title, body)

    def delete_note(self):
        note_id = int(input("Введите ID заметки для удаления: "))
        self.app.delete(note_id)

    def filter_notes_by_date(self):
        start_date = input("Введите начальную дату (ГГГГ-ММ-ДД): ")
        end_date = input("Введите конечную дату (ГГГГ-ММ-ДД): ")
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
            filtered_notes = self.app.filter_notes_by_date(start_date, end_date)
            if not filtered_notes:
                print("Нет заметок в заданном диапазоне дат.")
            else:
                self.app.list_notes(filtered_notes)
        except ValueError:
            print("Неверный формат даты. Используйте ГГГГ-ММ-ДД.")

    def print_menu(self):
        print("Команды:")
        print(" - add: Добавить новую заметку")
        print(" - list: Вывести список заметок")
        print(" - update: Обновить существующую заметку")
        print(" - delete: Удалить заметку")
        print(" - filter: Фильтровать заметки по дате")
        print(" - exit: Завершить программу")

if __name__ == '__main__':
    main = Main()
    main.run()

