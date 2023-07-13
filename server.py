
from flask import Flask, render_template
import os

# Constantes
PORT = 8080
APP_NAME = "APP-Runner! "
MESSAGE = f"Olá, {os.environ.get('NAME', 'BSP-CLOUD - Versão 003')}🐍🐧"

# Configuração do aplicativo Flask
app = Flask(__name__)

# Rota principal
@app.route("/")
def root():
    print("Tratando requisição web. Retornando página HTML.")
    return render_template('index.html', message=MESSAGE)

# Inicialização do servidor
if __name__ == "__main__":
    print(f"{APP_NAME} iniciado. Acesse em http://localhost:{PORT}/")
    app.run(debug=True, host="0.0.0.0", port=PORT)



######################## versão 3 ################################
