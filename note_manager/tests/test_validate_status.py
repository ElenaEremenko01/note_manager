import unittest

from note_manager.utils.status_validator import validate_status


class TestNoteManager(unittest.TestCase):
    def test_valid_dates(self):
        self.assertTrue(validate_status('новая'))
        self.assertTrue(validate_status('в процессе'))
        self.assertTrue(validate_status('выполнено'))
    def test_invalid_dates(self):
        self.assertFalse(validate_status('отложено'))
        self.assertFalse(validate_status('in work'))
        self.assertFalse(validate_status('done'))

if __name__ == '__main__':
    unittest.main()