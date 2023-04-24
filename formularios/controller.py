from flask import Flask, request

aplicacao = Flask(__name__)

@aplicacao.route('/meunome', methods=['POST', 'GET'])
def escrever_nome():
    print('Tratador de requisição.')
    if request.method == 'POST':
        print('Tratanto um post.')
        nome = request.form['nome_usuario']
    else:
        print('Tratando um get.')
        nome = request.args.get('nome_usuario')
    return "Seu nome é: " + nome

if __name__ == '__main__':
    aplicacao.run(host='0.0.0.0', port=5000)