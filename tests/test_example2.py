from example2 import __version__
from example2.example import Example


def test_version():
    assert __version__ == '0.1.0'

def test_request():
    ex = Example()
    assert ex.check_request("https://google.com")==200
    pass
