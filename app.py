from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # Intenta leer una variable de entorno para demostrar configuración
    target = os.environ.get('TARGET', 'Mundo')
    return f"¡Hola {target}! Esta es la versión 1.0 (Segura)\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)