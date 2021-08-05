from app import __version__


def test_version():
    assert __version__ == '0.1.0'


def test_hello_world():
    from main import hello_world
    assert hello_world() == {"Hello": "World"}
