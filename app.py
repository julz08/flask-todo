from flask import Flask, render_template, request
from tinydb import TinyDB, Query

app = Flask(__name__)
db=TinyDB('db.json')

@app.route('/', methods=['GET', 'POST'])
def todo():
    todo = request.form.get('todo')
    if todo:
        db.insert({'todo':todo})
    todos= db.all()
    return render_template('index.html', todos=todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)