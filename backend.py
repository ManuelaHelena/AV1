from config import *
from modelo import Cachorro 


@app.route("/")
def padrao():
    return "backend operante"

@app.route("/listar_cachorros")
def listar_cachorros():
    cachorros = db.session.query(Cachorro).all()
    retorno = []
    for p in cachorros:
        retorno.append(p.json())
    resposta = jsonify(retorno)
    return resposta

app.run(debug = True )