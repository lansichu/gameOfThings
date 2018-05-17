from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'lansi'}
	games = [
		{
			'id': 1,
			'gameMaster': {'username': 'lansi'},
			'prompt': 'What should you not to say to your mom?',
			'started': False
		},
		{
			'id': 2,
			'gameMaster': {'username': 'patrick'},
			'prompt': 'What do you need when you are alone?',
			'started': True
		}
	]
	return render_template('index.html', title='Home', user=user, games=games)
