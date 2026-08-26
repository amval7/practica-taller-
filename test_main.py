import pytest
from fastapi.testclient import TestClient
from main import app

# Creamos el cliente de pruebas que interactúa con nuestra app
client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["mensaje"] == "API de Calculadora Operativa"
    assert data["estado"] == "ok"

def test_sumar():
    response = client.get("/sumar?a=10&b=5")
    assert response.status_code == 200
    assert response.json()["resultado"] == 15.0

def test_restar():
    response = client.get("/restar?a=20&b=8")
    assert response.status_code == 200
    assert response.json()["resultado"] == 12.0

def test_multiplicar():
    response = client.get("/multiplicar?a=4&b=3")
    assert response.status_code == 200
    assert response.json()["resultado"] == 12.0

def test_dividir_exitoso():
    response = client.get("/dividir?a=10&b=2")
    assert response.status_code == 200
    assert response.json()["resultado"] == 5.0

def test_dividir_por_cero():
    response = client.get("/dividir?a=10&b=0")
    assert response.status_code == 400
    assert response.json()["detail"] == "No es posible dividir por cero"

def test_es_par():
    # Caso 1: Número par
    response_par = client.get("/es-par/4")
    assert response_par.status_code == 200
    assert response_par.json()["es_par"] is True
    
    # Caso 2: Número impar
    response_impar = client.get("/es-par/7")
    assert response_impar.status_code == 200
    assert response_impar.json()["es_par"] is False

def test_potencia():
    response = client.get("/potencia?base=2&exponente=3")
    assert response.status_code == 200
    assert response.json()["resultado"] == 8.0

def test_potencia_exponente_negativo():
    response = client.get("/potencia?base=2&exponente=-1")
    assert response.status_code == 400
    assert response.json()["detail"] == "Exponente negativo no soportado"

def test_raiz_cuadrada_valida():
    response = client.get("/raiz-cuadrada/16")
    assert response.status_code == 200
    assert response.json()["resultado"] == 4.0

def test_raiz_cuadrada_negativa():
    response = client.get("/raiz-cuadrada/-9")
    assert response.status_code == 400
    assert response.json()["detail"] == "No se admiten números negativos"

def test_porcentaje():
    response = client.get("/porcentaje?total=200&porcentaje=15")
    assert response.status_code == 200
    assert response.json()["resultado"] == 30.0

def test_porcentaje_negativo():
    response = client.get("/porcentaje?total=-50&porcentaje=10")
    assert response.status_code == 400
    assert response.json()["detail"] == "Los valores deben ser positivos"