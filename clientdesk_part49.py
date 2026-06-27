# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: ClientDesk
import unittest
from clientdesk import ClientDesk, Contact

class TestClientDeskEdgeCases(unittest.TestCase):
    def setUp(self):
        self.app = ClientDesk()
    
    def test_update_nonexistent_contact(self):
        with self.assertRaises(KeyError):
            self.app.update_contact("nonexistent_id", {"name": "New Name"})
    
    def test_delete_nonexistent_contact(self):
        with self.assertRaises(KeyError):
            self.app.delete_contact("nonexistent_id")
    
    def test_update_empty_name(self):
        contact = Contact(name="Old Name", phone="1234567890")
        self.app.add_contact(contact)
        updated = self.app.update_contact(contact.id, {"name": "", "phone": "1234567890"})
        self.assertEqual(updated.name, "")

if __name__ == "__main__":
    unittest.main()
