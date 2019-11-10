from unittest import TestCase

from helloworld.greeter import say_hello


class TestSayHello(TestCase):

    def test_say_hello(self):
        self.assertEqual(
            'Hello, Bob!',
            say_hello('Bob')
        )

    def test_no_name(self):
        self.assertIsNone(say_hello())
