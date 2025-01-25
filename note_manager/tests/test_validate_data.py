import unittest

from note_manager.utils.data_validator import validate_data

class TestNoteManager(unittest.TestCase):
    def test_valid_dates(self):
        self.assertTrue(validate_data('26.01.2023'))
        self.assertTrue(validate_data('26.02.2026'))
        self.assertTrue(validate_data('12.03.2028'))
    def test_invalid_dates(self):
        self.assertFalse(validate_data('15/06/2025'))
        self.assertFalse(validate_data('23/01/2026'))
        self.assertFalse(validate_data('23.13.2028'))

if __name__ == '__main__':
    unittest.main()