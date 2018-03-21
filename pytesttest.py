import pytest


@pytest.mark.xfail
def test_upper():
    assert 'foo'.upper() == 'FoO'


def test_isupper():
    assert 'FOO'.isupper()
    assert not 'Foo'.isupper()


def test_split():
    s = 'hello world'
    assert s.split() == ['hello', 'wrld']
    # check that s.split fails when the separator is not a string
    with pytest.raises(TypeError):
        s.split(2)