import main


def test_hello():
    # http://127.0.0.1:8000
    assert main.hello_world() == {"Hello": "World"}


def test_greet_something():
    # http://127.0.0.1:8000/Hey
    assert main.greet_something("Hey") == {"Hey": "World"}
    # http://127.0.0.1:8000/Hey?something=You
    assert main.greet_something("Hey", "You") == {"Hey": "You"}
