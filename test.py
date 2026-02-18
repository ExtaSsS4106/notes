from src.notes import funcs
import unittest

funcs.db_start()
class Test(unittest.TestCase):
    def test_get_notes(self):
        notes = funcs.get_notes()
        
        self.assertIsInstance(notes, list)
        
        self.assertIsNotNone(notes)
        if notes:
            for n in notes:
                self.assertIsInstance(n.get("id"), int)
                self.assertIsInstance(n.get("note"), str)
        else:
            self.assertListEqual(notes, [])
    
    def test_add_note(self):
        initial_notes = funcs.get_notes()
        initial_count_before = len(initial_notes)
        
        funcs.add_note("test", "text_test")
        
        
        initial_notes = funcs.get_notes()
        initial_count_now = len(initial_notes)
        
        self.assertEqual(initial_count_now, initial_count_before+1)
    
    def test_update_note(self):
        notes = funcs.get_notes()
        last_note = notes[-1]
        new_text = "new test text from test_update_note"
        funcs.update_note_text(last_note.get("id"), new_text)
        
        self.assertEqual(funcs.get_note_text(last_note.get("id")), new_text)

    def test_delete_note(self):
        notes = funcs.get_notes()
        last_note = notes[-1]
        
        funcs.delete_note(last_note.get("id"))

        notes = funcs.get_notes()
        new_last_note = notes[-1]      
        
        self.assertEqual(new_last_note.get("id"), last_note.get("id") - 1)
    
    def test_get_note_text(self):
        funcs.get_note_text("note_id")
if __name__ == '__main__':
    unittest.main()
