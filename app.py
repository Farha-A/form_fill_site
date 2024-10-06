from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
 return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
 name = request.form['name']
 id = request.form['id']
 age = request.form['age']
 mail = request.form['mail']
 return render_template('res.html', name=name, age=age, id=id, mail=mail)



if __name__ == '__main__':
 app.run(debug=True)