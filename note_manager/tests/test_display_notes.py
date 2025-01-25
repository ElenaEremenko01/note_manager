import unittest

from note_manager.interface.display_notes import display_notes


class TestNoteManager(unittest.TestCase):
    def test_display_notes(self):
        notes = [{'username': 'Test',
                  'title': 'Test Note',
                  'content': 'This is test',
                  'status': 'new',
                  'created_date': '01.01.2025',
                  'issue_date': '10.01.2026'}]
        data = display_notes(notes)
        self.assertEqual(data)

if __name__ == '__main__':
    unittest.main()
