import unittest
class PaymentTest(unittest.TestCase):
    def test_paymentindollo(self):
        print("This is payment in dollor test")
        self.assertTrue(True)

    def test_paymentinrupess(self):
        print("This is payment in rupees test")
        self.assertTrue(True)

if __name__ == '__main__':
     unittest.main()
