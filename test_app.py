import unittest

from app import saudacao


class TestSaudacao(unittest.TestCase):
    def test_com_nome(self):
        self.assertEqual(saudacao("Ana"), "Olá, Ana!")

    def test_sem_nome(self):
        self.assertEqual(saudacao("  "), "Olá!")
        self.assertEqual(saudacao(None), "Olá!")


if __name__ == "__main__":
    unittest.main()
