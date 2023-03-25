from src.pre_built.counter import count_ocurrences
from unittest.mock import mock_open, patch
import pytest


@pytest.fixture
def read():
    return """
    Linguagem de Programação é uma linguagem escrita e formal
    que especifica um conjunto de instruções e regras usadaspara
    gerar programas (software). Um software pode ser desenvolvido
    para rodar em um computador, dispositivo móvel
    ou em qualquer equipamento que permita sua execução.
    """


def test_counter(read):
    with patch("builtins.open", mock_open(read_data=read)):
        assert count_ocurrences("path/path", "linguagem") == 2
