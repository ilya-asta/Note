import json
from datetime import datetime

from Note import Note


class NoteDataStorage:
    def __init__(self, filename):
        self.filename = filename

    def save_notes(self, notes):
        with open(self.filename, 'w') as file:
            # Сериализуем заметки в формат JSON и записываем в файл
            notes_data = [
                {
                    'identifier': note.identifier,
                    'title': note.title,
                    'body': note.body,
                    'created_at': note.created_at.isoformat(),
                }
                for note in notes
            ]
            json.dump(notes_data, file)

    def load_notes(self):
        notes = []
        try:
            with open(self.filename, 'r') as file:
                notes_data = json.load(file)
                for note_data in notes_data:
                    # Если в данных нет 'created_at', создаем Note без этого параметра
                    note = Note(
                        identifier=note_data['identifier'],
                        title=note_data['title'],
                        body=note_data['body'],
                    )
                    if 'created_at' in note_data:
                        note.created_at = datetime.fromisoformat(note_data['created_at'])
                    notes.append(note)
        except FileNotFoundError:
            notes = []
        return notes