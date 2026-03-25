from flask import Flask, render_template

app = Flask(__name__)

diction = {
    'title' : 'Анкета',
    'surname' : 'Watny',
    'name' : 'Mark',
    'education' : 'выше среднего',
    'profession' : 'штурман марсохода',
    'sex' : 'male',
    'motivation' : 'Всегда мечтал застрять на Марсе!',
    'ready' : 'True'
}

@app.route('/answer')
def answer():
    return render_template('answer.html', title='Заполнение анкеты')

@app.route('/auto_answer')
def auto_answer():
    return render_template('auto_answer.html', diction=diction)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
