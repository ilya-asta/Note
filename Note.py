from datetime import datetime
class Note:
    def __init__(self, identifier, title, body):
        self.identifier = identifier
        self.title = title
        self.body = body

        # Получите текущую дату и время при создании заметки
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update(self, new_title, new_body):
        self.title = new_title
        self.body = new_body

    @staticmethod
    def create_note(identifier, title, body):
        # Получите текущую дату и время
        from datetime import datetime
        created_at = datetime.now()

        # Создайте объект заметки
        note = Note(identifier, title, body, created_at)

        return note

    # Эта функция создает объект Note с указанными параметрами и возвращает его.
    @staticmethod
    def read_notes(notes):
        for note in notes:
            print(f"ID: {note.identifier}")
            print(f"Title: {note.title}")
            print(f"Body: {note.body}")
            print(f"Created At: {note.created_at}\n")

    #   notes: Список объектов заметок, который передается в функцию.
    # Эта функция принимает список заметок и выводит информацию
    # о каждой заметке, включая идентификатор, заголовок, тело и дату создания.
    @staticmethod
    def update_note(note, new_title, new_body):
        note.title = new_title
        note.body = new_body
    #     note: Объект заметки, который требуется обновить.
    # new_title: Новый заголовок для заметки.
    # new_body: Новое тело заметки.
    # Эта функция обновляет заголовок и тело существующей заметки на новые значения.

    @staticmethod
    def delete_note(notes, note_to_delete):
        notes.remove(note_to_delete)

#         notes: Список заметок, в котором нужно удалить заметку.
#         note_to_delete: Заметка, которую нужно удалить.
#           Эта функция удаляет выбранную заметку из списка заметок.


