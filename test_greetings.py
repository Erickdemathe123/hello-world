import unittest
from main import get_greeting


class TestGreetings(unittest.TestCase):
    def test_portuguese(self):\
        self.assertEqual(get_greeting("pt"), "Olá, Mundo!")

    def test_english(self):
        self.assertEqual(get_greeting("en"), "Hello, World!")

    def test_spanish(self):
        self.assertEqual(get_greeting("es"), "¡Hola, Mundo!")

    def test_french(self):
        self.assertEqual(get_greeting("fr"), "Bonjour, le Monde!")

    def test_german(self):
        self.assertEqual(get_greeting("de"), "Hallo, Welt!")

    def test_italian(self):
        self.assertEqual(get_greeting("it"), "Ciao, Mondo!")

    def test_japanese(self):
        self.assertEqual(get_greeting("jp"), "こんにちは、世界！")

    def test_russian(self):
        self.assertEqual(get_greeting("ru"), "Привет, мир!")

    def test_chinese(self):
        self.assertEqual(get_greeting("zh"), "你好，世界！")

    def test_invalid_language(self):
        self.assertEqual(get_greeting("xx"), "Idioma não suportado")

if __name__ == "__main__":
    unittest.main()
