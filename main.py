from flask import Flask, render_template, request  #Importa a classe Flask do módulo Flask

app = Flask(__name__)  #Cria uma instância da aplicação Flask

@app.route('/')  #Define uma rota padrão (página inicial) da aplicação
def index(): #Define uma função chamada index
    return render_template('index.html') #Retorna o conteúdo do arquivo HTML chamado 'index.html'

@app.route('/verificar', methods = ['POST'])  #Define uma rota '/verificar' que aceita apenas requisições POST
def verificar(): #Define uma função chamada verificar
    usuario = (request.form['usuario'])
    senha = (request.form['senha'])
    if usuario == senha:
        resultado = "ERRO! O usuário não pode ser igual a senha."
    else:
        resultado = "Ok!"
    return render_template('index.html',resultado = resultado)

if __name__ == '__main__':  #Verifica se este arquivo está sendo executado diretamente
    app.run(debug = True)  #Inicia o servidor de desenvolvimento do Flask com modo de depuração ativado