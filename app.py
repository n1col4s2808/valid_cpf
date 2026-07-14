from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    
    if request.method == 'POST':
        cpf = request.form['cpf']
        resultado = validar_cpf(cpf)
    
    return render_template('index.html', resultado=resultado)

def validar_cpf(cpf):
    if len(cpf) != 11:
        return 'Tamanho inválido!'
    if not cpf.isdigit():
        return 'Digite apenas números!'
    if len(set(cpf)) == 1:
        return 'CPF inválido!'
    
    soma = 0
    peso = 10
    for numero in cpf[:9]:
        soma += int(numero) * peso
        peso -= 1
    digito1 = (soma * 10) % 11
    if digito1 > 9:
        digito1 = 0

    soma = 0
    peso = 11
    for numero in cpf[:10]:
        soma += int(numero) * peso
        peso -= 1
    digito2 = (soma * 10) % 11
    if digito2 > 9:
        digito2 = 0

    if str(digito1) == cpf[9] and str(digito2) == cpf[10]:
        return 'CPF VÁLIDO '
    else:
        return 'CPF INVÁLIDO'

if __name__ == '__main__':
    app.run(debug=True)