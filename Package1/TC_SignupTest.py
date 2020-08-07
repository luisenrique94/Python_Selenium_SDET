import unittest
class SignupTest(unittest.TestCase):
    def test_signbyEmail(self):
        print("This is sign by email test")
        self.assertTrue(True)

    def test_signbyFacebook(self):
        print("This is sign by facebook test")
        self.assertTrue(True)


    def test_signbyTwitter(self):
        print("This is sign by twitter test")
        self.assertTrue(True)

if __name__ == '__main__':
     unittest.main()
