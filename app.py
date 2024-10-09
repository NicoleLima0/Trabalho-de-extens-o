from flask import Flask, render_template, request, redirect, url_for
# import pdb;

app = Flask(__name__)

@app.route('/')
def landing_page():
    return render_template('index.html')

@app.route('/cadastro', methods=['POST'])
def cadastro_animal():
    name = request.form['name']
    species = request.form['species']
    age = request.form['age']
    tel = request.form['tel']

    # pdb.set_trace();  

    print(f"Animal Cadastrado: Nome={name}, Espécie={species}, Idade={age}, Telefone={tel}")
    return redirect(url_for('landing_page'))

if __name__ == '__main__':
    app.run(debug=True)