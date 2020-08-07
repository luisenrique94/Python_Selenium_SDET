import  unittest
from Package1.TC_LoginTest import LoginTest
from Package1.TC_SignupTest import SignupTest
from Package2.TC_PaymentReturnsTest import PaymentReturnsTest
from Package2.TC_PaymentTest import PaymentTest
#get all test from
tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3=unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)
tc4=unittest.TestLoader().loadTestsFromTestCase(PaymentTest)

#creating test suite
sanityTestSuite=unittest.TestSuite([tc1,tc2]) #sanyti test suite
functionalTestSuite=unittest.TestSuite([tc3,tc4]) #functional  test suite
masterTestSuite = unittest.TestSuite([tc1,tc2,tc3,tc4]) #master test suite
unittest.TextTestRunner(verbosity=2).run(masterTestSuite)
