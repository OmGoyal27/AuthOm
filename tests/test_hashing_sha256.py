from main import hash_password_sha256
import unittest

class TestHashingSHA256(unittest.TestCase):
    def test_hash_password_sha256(self):

        self.assertEqual(hash_password_sha256("password"), "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8")

        self.assertEqual(hash_password_sha256(""), "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")
        
        self.assertEqual(hash_password_sha256("Om Goyal"), "7ed040b269b98df0f8756dcbf525fad236df576caec2d6fa9ca3ffcc9a7249a4")

        self.assertEqual(hash_password_sha256("134$%343vdfr%$dvGFDxc  y4d^%  D d2[[]:{};.';.;lK<D896d"), "3090ba51b0addaa02c8e30a84b7eae07ec34c0d8bf6e72873b017c36dd21d51b")