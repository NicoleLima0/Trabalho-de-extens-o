from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
import json
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

DATA_FILE = 'animals.json'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def load_animals():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_animals(animals):
    with open(DATA_FILE, 'w') as f:
        json.dump(animals, f)

@app.route('/')
def landing_page():
    animals = load_animals()
    return render_template('index.html', animals=animals)

@app.route('/cadastro', methods=['POST'])
def cadastro_animal():
    animals = load_animals()
    
    name = request.form['name']
    species = request.form['species']
    sex = request.form['sex']
    age = request.form['age']
    tel = request.form['tel']

    if 'image' not in request.files:
        return 'Nenhuma imagem foi enviada', 400

    image = request.files['image']
    
    if image.filename == '':
        return 'Nenhuma imagem foi selecionada', 400

    if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(image_path)
        image_path = image_path.replace("\\", "/")
        
        animal = {
            'name': name,
            'species': species,
            'sex': sex,
            'age': age,
            'tel': tel,
            'image': image_path
        }
        animals.append(animal)
        save_animals(animals)
        print(f"Animal cadastrado: {animal}")
    
    return redirect(url_for('landing_page'))

@app.route('/remover-animal', methods=['POST'])
def remover_animal():
    animals = load_animals()
    data = request.get_json()
    animal_name = data.get('name')

    animal_to_remove = None
    for animal in animals:
        if animal['name'] == animal_name:
            animal_to_remove = animal
            break

    if not animal_to_remove:
        return jsonify({'success': False, 'message': 'Animal não encontrado'}), 404

    image_path = animal_to_remove['image']
    if os.path.exists(image_path):
        try:
            os.remove(image_path)
            print(f"Imagem removida: {image_path}")
        except Exception as e:
            print(f"Erro ao remover a imagem: {e}")
            return jsonify({'success': False, 'message': 'Erro ao remover a imagem'}), 500


    animals = [animal for animal in animals if animal['name'] != animal_name]
    save_animals(animals)

    return jsonify({'success': True})

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)