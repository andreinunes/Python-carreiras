from re import DEBUG
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

VAGAS = [
  {'id':1,
    'titulo': 'Analista de Suporte',
  'localidade': 'São Paulo',
  'salario': 'R$ 3.500,00',},
  {'id':2,
    'titulo': 'Analista de Dados',
  'localidade': 'Rio de Janeiro',
  'salario': 'R$ 1.500,00',},
  {'id':3,
    'titulo': 'Cientista de Dados',
  'localidade': 'Ceará',
  'salario': 'R$ 4.500,00',},
  {'id':4,
    'titulo': 'Desenvolvedor Backend',
  'localidade': 'Pará',
  'salario': 'R$ 12.500,00',},
  {'id':5,
    'titulo': 'Desenvolvedor Frontend',
  'localidade': 'Amapá',
  'salario': 'R$ 321.500,00',}
  
]

@app.route('/')
def hello():
  return render_template("home.html", vagas=VAGAS)


@app.route('/vagas')
def lista_vagas():
  return jsonify(VAGAS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
