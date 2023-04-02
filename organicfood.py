from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/novo_consumidor')
def novo_consumidor():
    return render_template('novo_consumidor.html')


@app.route('/novo_produtor')
def novo_produtor():
    return render_template('novo_produtor.html')




# @app.route('/criar', methods=['POST', ])
# def criar():
#     nome = request.form['nome']
#     categoria = request.form['categoria']
#     console = request.form['console']
#     jogo = Jogos.query.filter_by(nome=nome).first()
#     if jogo:
#         flash("Jogo já existe.")
#         return redirect(url_for('index'))
#     novo_jogo = Jogos(nome=nome, categoria=categoria, console=console)
#     db.session.add(novo_jogo)
#     db.session.commit()
#
#     return redirect(url_for('index'))




app.run()
