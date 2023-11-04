from datetime import datetime
import click
from Note import Note
from NoteDataStorage import NoteDataStorage


class NoteApp:
    def __init__(self):
        self.notes = []

    def add(self, title, body):
        """Добавить новую заметку."""
        note = Note(identifier=len(self.notes) + 1, title=title, body=body)
        self.notes.append(note)

    def list_notes(self, notes=None):
        """Список заметок."""
        notes_to_display = notes if notes is not None else self.notes

        if not notes_to_display:
            print("Список заметок пуст.")
        else:
            for note in notes_to_display:
                print(f"ID: {note.identifier}")
                print(f"Title: {note.title}")
                print(f"Body: {note.body}")
                print(f"Created At: {note.created_at}\n")

    def update(self, note_id, title, body):
        """Обновить существующую заметку."""
        found = False
        for note in self.notes:
            if note.identifier == note_id:
                note.title = title
                note.body = body
                found = True
                break

        if found:
            print(f"Заметка с ID {note_id} обновлена.")
        else:
            print(f"Заметка с ID {note_id} не найдена.")

    def delete(self, note_id):
        """Удалить заметку."""
        found = None
        for note in self.notes:
            if note.identifier == note_id:
                found = note
                break

        if found:
            self.notes.remove(found)
            print(f"Заметка с ID {note_id} удалена.")
        else:
            print(f"Заметка с ID {note_id} не найдена.")

    def save_notes_to_file(self):
        note_data_storage = NoteDataStorage("notes.json")
        note_data_storage.save_notes(self.notes)


    def load_notes_from_file(self):
        note_data_storage = NoteDataStorage("notes.json")
        self.notes = note_data_storage.load_notes()

    def filter_notes_by_date(self, start_date, end_date):
        filtered_notes = []
        for note in self.notes:
            if start_date <= note.created_at <= end_date or start_date <= note.updated_at <= end_date:
                filtered_notes.append(note)
        return filtered_notes
#     Этот метод filter_notes_by_date принимает два аргумента:
#     start_date и end_date, которые определяют начало и конец периода
#     , на который нужно фильтровать заметки.
#     Метод проходит по всем заметкам и добавляет те,
#     которые попадают в указанный временной диапазон, в новый список filtered_notes.

@click.group()
def notes():
    """Управление заметками."""

@notes.command()
@click.option('--title', prompt='Заголовок', help='Заголовок заметки')
@click.option('--body', prompt='Тело', help='Тело заметки')
@click.option('--start_date', help='Начальная дата в формате ГГГГ-ММ-ДД')
@click.option('--end_date', help='Конечная дата в формате ГГГГ-ММ-ДД')
def filter_by_date(start_date, end_date):
    if start_date and end_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        filtered_notes = app.filter_notes_by_date(start_date, end_date)
        app.list_notes(filtered_notes)
    else:
        print("Введите начальную и конечную даты для фильтрации.")
def add(title, body):
    app.add(title, body)

@notes.command()
def list():
    app.list_notes()

@notes.command()
@click.argument('note_id', type=int)
@click.option('--title', help='Новый заголовок заметки')
@click.option('--body', help='Новое тело заметки')
def update(note_id, title, body):
    app.update(note_id, title, body)

@notes.command()
@click.argument('note_id', type=int)
def delete(note_id):
    app.delete(note_id)

if __name__ == '__main__':
    app = NoteApp()
    notes()




