import unittest
from uuid import UUID
from note_manager.utils.uuid_geneator import generate_unique_id

class TestNoteManager(unittest.TestCase):
    def test_generate_id(self):
        unique_id = generate_unique_id()
        self.assertIsInstance(unique_id, str)
        try:
            uuid_obj = UUID(unique_id, version=4)
        except ValueError:
            self.fail('Ошибка')
        self.assertEqual(uuid_obj.version, 4)

        def test_unique(self):
            ids = {unique_id for _ in range(1000)}
            self.assertEqual(len(ids), 1000)


if __name__ == '__main__':
    unittest.main()

