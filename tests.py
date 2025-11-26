import pytest
from app import sumar
from app import multiplicar

def test_suma_positivos():
    assert sumar(10, 20) == 30

def test_suma_negativos():
    assert sumar(-5, -5) == -10
    

    
    