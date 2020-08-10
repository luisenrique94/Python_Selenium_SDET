import pytest

@pytest.fixture()
def setup():
    print("once before every method")
def testMethod1():
    print("This is test method1")

def testMethod2():
    print("this is test method2")

