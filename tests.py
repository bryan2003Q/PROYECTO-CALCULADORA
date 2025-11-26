#import pytest
from app import sumar, restar, multiplicar, dividir


# Pruebs de suma
def test_suma_positivos():
    assert sumar(10, 20) == 30

def test_suma_negativos():
    assert sumar(-5, -5) == -10
    
def test_suma_mixta():
    assert sumar(10, -3) == 7
    
#Pruebas de resta    
def test_resta_positivos():
    assert restar(10, 5) == 5

def test_resta_negativos():
    assert restar(-10, -5) == -5
    
def test_resta_mixta():
    assert restar(10, -5) == 15    
    
#Pruebas de multiplicación
    
def test_multiplicacion_positivos():
    assert multiplicar(4, 3) == 12

def test_multiplicacion_negativos():
    assert multiplicar(-4, -3) == 12

def test_multiplicacion_mixta():
    assert multiplicar(4, -3) == -12

#Pruebas división
def test_division_positivos():
    assert dividir(10, 2) == 5

def test_division_negativos():
    assert dividir(-10, -2) == 5

def test_division_mixta():
    assert dividir(10, -2) == -5

def test_division_por_cero():
    assert dividir(10, 0) == "Error: No se puede dividir para cero"