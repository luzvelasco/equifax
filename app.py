from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():

    target = os.environ.get('TARGET', 'Mundo')
    return f"Proyecto {target}. Esta es la versión segura\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)