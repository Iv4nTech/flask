from flask import Flask, render_template, redirect, url_for, abort

app = Flask(__name__)

@app.route('/')
def start():
    return 'Hola buenas, como estás?'

@app.route('/home')
def render_home():
    return 'Estás en la página principal de la web! :)'

@app.route('/holacaracola/<user>')
@app.route('/inicio_sesion/<user>')
def iniciar_sesion(user):
    return f'Hola, {user}'

@app.route('/mostrar_numero/<int:numero>')
def sumar(numero):
    return f" La suma es de: {numero + 5}"

@app.route('/mostrar_template')
def mostrar():
    return render_template('main.html', autor='Iván Gómez')

@app.route('/redireccionar')
def redireccion():
    return redirect(url_for('start'))

@app.route('/not_found')
def error_404():
    return abort(404)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error=error), 404