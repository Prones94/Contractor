from unittest import TestCase, main as unittest_main
from app import app

class CoffeeBeans(TestCase):
    def setUp(self):
        self.client = app.test_client()

        app.cofig['TESTING'] = True

    def test_index(self):
        """Test coffee bean homepage."""
        result = self.client.get('/')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Coffee Bean', result.data)

    def test_edit(self):
        '''Test edit page'''
        result = self.client.get('/beans')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Edit Bean', result.data)

    def test_submit(self):
        '''Test submit page'''
        result = self.client.get('/new_beans')
        self.assertEqual(result.status,'200 OK')
        self.assertIn(b'Show Bean', result.data)
if __name__='__main__':
    unittest_main()