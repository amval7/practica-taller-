from fastapi import FastAPI, HTTPException

app = FastAPI(title="Calculadora API - CI Demo", version="1.0.0")

@app.get("/")
def home():
    """Ruta raíz de bienvenida y comprobación de estado."""
    return {"mensaje": "API de Calculadora Operativa", "estado": "ok"}

@app.get("/sumar")
def sumar(a: float, b: float):
    """Suma dos números."""
    return {"operacion": "suma", "a": a, "b": b, "resultado": a + b}

@app.get("/restar")
def restar(a: float, b: float):
    """Resta dos números."""
    return {"operacion": "resta", "a": a, "b": b, "resultado": a - b}

@app.get("/multiplicar")
def multiplicar(a: float, b: float):
    """Multiplica dos números."""
    return {"operacion": "multiplicacion", "a": a, "b": b, "resultado": a * b}

@app.get("/dividir")
def dividir(a: float, b: float):
    """Divide a entre b con validación de división por cero."""
    if b == 0:
        raise HTTPException(status_code=400, detail="No es posible dividir por cero")
    return {"operacion": "division", "a": a, "b": b, "resultado": a / b}

@app.get("/es-par/{numero}")
def es_par(numero: int):
    """Determina si un número entero es par o impar."""
    return {"numero": numero, "es_par": (numero % 2 == 0)}