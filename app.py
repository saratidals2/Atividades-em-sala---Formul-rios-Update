from flask import Flask, render_template, jsonify, request
import dados

app = Flask(__name__)

@app.route("/biblioteca", methods = ['GET'])
def biblioteca():
    biblio = dados.carregar_do_arquivo()

    return render_template("index.html", biblio = biblio)


@app.route("/forms", methods=['GET'])
def forms():
    return render_template("formulario.html")


@app.route("/salvar_livro", methods=['POST'])
def salvar_livro():

    titulo = request.form['titulo']
    autor = request.form['autor']
    ano = request.form['ano']

    livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano
    }

    dados.salvar_livro(livro)

    return "Livro cadastrado com sucesso!"


@app.route("/alterar", methods=['GET'])
def alterar():
    return render_template("alterar.html")


@app.route("/atualizar_livro", methods=['POST'])
def atualizar_livro():

    codigo = request.form['codigo']
    titulo = request.form['titulo']
    autor = request.form['autor']
    ano = request.form['ano']

    dados.atualizar_livro(codigo, titulo, autor, ano)

    return biblioteca()

@app.route("/api/biblio")
def listar_livro():
    lista = dados.carregar_do_arquivo()
    return  jsonify(lista)

@app.route("/api/criar", methods= ['POST'])
def criar_livro(): 
    lista = dados.carregar_do_arquivo()
    novo_livro = request.get_json()
    lista.append(novo_livro)
    dados.salvar_no_arquivo(lista)
    return "Livro Cadastrado", 201

@app.route("/api/deletar/<id>", methods=['DELETE'])
def deletar_livros(id = None):
    lista = dados.carregar_do_arquivo()
    for livro in lista:
        if livro["id"] == id:
            lista.remove(livro)
    dados.salvar_no_arquivo(lista)  
    return "Livro deletado", 203

@app.route("/api/alterar/<id>")      
if __name__ == "__main__":
    app.run()

