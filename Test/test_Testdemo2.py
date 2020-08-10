import pytest
@pytest.yield_fixture()
def setup():
    print("once before every method")
    yield
    print("one after every method")

def testMethod1():
    print("this is test method 1")
def testMethod2():
    print("this is ted method 2")


