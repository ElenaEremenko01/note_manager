import unittest

from note_manager.data.save_notes_json import save_notes_to_json
from note_manager.data.load_notes_from_file import load_notes_from_file
from note_manager.data.save_notes_to_file import save_notes_to_file



class TestNoteManager(unittest.TestCase):
    def test_save_and_load_notes(self):
        notes = [{'username': 'Test',
                  'title': 'Test Note',
                  'content': 'This is test',
                  'status': 'new',
                  'created_date': '01.01.2025',
                  'issue_date': '10.01.2026'}]
        test_filename = 'test_notes.txt'
        save_notes_to_file(notes, test_filename)
        loaded_notes = load_notes_from_file(test_filename)
        self.assertEqual(notes, loaded_notes)


if __name__ == '__main__':
    unittest.main()
