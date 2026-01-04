from flask import Flask, render_template, redirect, url_for, abort, session, request

app = Flask(__name__)

app.secret_key = 'f3a6231a840fe5c8dc8931d9fa5da010cbbf54c9c5460302bd12b7e7e9c0a2ad'

@app.route('/')
def start():
    if 'username' in session:
        return f'El usuario {session['username']} ha iniciado sesion'
    return 'El ususario no inicio sesión'

@app.route('/login', methods=['GET', 'POST'])
def inicio_sesion():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('start'))
    return render_template('login.html')

@app.route('/logout')
def cerrar_sesion():
    session.pop('username', None)
    return redirect(url_for('start'))

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

@app.route('/prueba/<info>', methods=['GET', 'POST'])
def probar(info):
    return f'La información que he recibido es la siguiente: {info}'