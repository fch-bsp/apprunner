
# from flask import Flask
# import os

# PORT = 8080
# name = os.environ.get('NAME')
# if name == None or len(name) == 0:
#   name = "APP-Runner! Versão 001 👨‍💻"
# MESSAGE = "Olá , " + name + "‼️🐍🐧"
# print("Message: '" + MESSAGE + "'")

# app = Flask(__name__)


# @app.route("/")
# def root():
#   print("Handling web request. Returning message.")
#   result = MESSAGE.encode("utf-8")
#   return result


# if __name__ == "__main__":
#   app.run(debug=True, host="0.0.0.0", port=PORT)

# -*- coding: utf-8 -*-
"""
Este é um exemplo de aplicativo web simples usando Flask.
"""

from flask import Flask
import os

# Constantes
PORT = 8080
APP_NAME = "APP-Runner! Versão 001 👨‍💻"
MESSAGE = f"Olá, {os.environ.get('NAME', 'Desenvolvedor')}‼️🐍🐧"

# Configuração do aplicativo Flask
app = Flask(__name__)

# Rota principal
@app.route("/")
def root():
    print("Tratando requisição web. Retornando mensagem.")
    return MESSAGE.encode("utf-8")

# Inicialização do servidor
if __name__ == "__main__":
    print(f"{APP_NAME} iniciado. Acesse em http://localhost:{PORT}/")
    app.run(debug=True, host="0.0.0.0", port=PORT)
