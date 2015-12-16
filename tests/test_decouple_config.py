# coding: utf-8
from StringIO import StringIO

from casting import to_tuple
from decouple import Config, RepositoryEnv
from mock import patch
import pytest


ENVFILE = """
TEST_DEFAULT_DIVIDER_1=pepe,carl,jose
TEST_DEFAULT_DIVIDER_2=pepe, carl, jose
TEST_DEFAULT_DIVIDER_3= pepe , carl , jose
TEST_DEFAULT_DIVIDER_4=   pepe ,carl, jose
TEST_DEFAULT_DIVIDER_5=pepe,carl,jose,
TEST_CUSTOM_DIVIDER_1=pepe;carl;jose
TEST_CUSTOM_DIVIDER_2=pepe; carl; jose
TEST_CUSTOM_DIVIDER_3= pepe ; carl ; jose
TEST_CUSTOM_DIVIDER_4=   pepe ;carl; jose
TEST_CUSTOM_DIVIDER_5=pepe;carl;jose;
TEST_NESTED_DIVIDER_1=pepe,carl,jose;pablo,mark
TEST_NESTED_DIVIDER_2=pepe, carl, jose; pablo, mark
TEST_NESTED_DIVIDER_3= pepe , carl , jose; pablo , mark
TEST_NESTED_DIVIDER_4=   pepe ,carl, jose;  pablo,  mark
TEST_NESTED_DIVIDER_5=pepe,carl,jose;pablo,mark,
"""


@pytest.fixture(scope='module')
def config():
    with patch('decouple.open', return_value=StringIO(ENVFILE), create=True):
        return Config(RepositoryEnv('.env'))


def test_default_divider(config):
    expected = ('pepe', 'carl', 'jose')
    cast = to_tuple()

    assert expected == config('TEST_DEFAULT_DIVIDER_1', cast=cast)
    assert expected == config('TEST_DEFAULT_DIVIDER_2', cast=cast)
    assert expected == config('TEST_DEFAULT_DIVIDER_3', cast=cast)
    assert expected == config('TEST_DEFAULT_DIVIDER_4', cast=cast)
    assert expected == config('TEST_DEFAULT_DIVIDER_5', cast=cast)


def test_custom_divider(config):
    expected = ('pepe', 'carl', 'jose')
    cast = to_tuple(delimiter=';')

    assert expected == config('TEST_CUSTOM_DIVIDER_1', cast=cast)
    assert expected == config('TEST_CUSTOM_DIVIDER_2', cast=cast)
    assert expected == config('TEST_CUSTOM_DIVIDER_3', cast=cast)
    assert expected == config('TEST_CUSTOM_DIVIDER_4', cast=cast)
    assert expected == config('TEST_CUSTOM_DIVIDER_5', cast=cast)


def test_nested_divider(config):
    expected = (('pepe', 'carl', 'jose'), ('pablo', 'mark'))
    cast = to_tuple(delimiter=';,')

    assert expected == config('TEST_NESTED_DIVIDER_1', cast=cast)
    assert expected == config('TEST_NESTED_DIVIDER_2', cast=cast)
    assert expected == config('TEST_NESTED_DIVIDER_3', cast=cast)
    assert expected == config('TEST_NESTED_DIVIDER_5', cast=cast)
