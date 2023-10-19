from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Usaremos um banco de dados SQLite em memória para este exemplo.
# Em um cenário de produção, você pode especificar um arquivo no sistema de arquivos.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'

db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(80), unique=True, nullable=False)
    conteudo = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo

@app.route('/items/<id>', methods=['GET'])
def get_item(id):
    item = Item.query.get(id)
    item_dict = item.__dict__
    item_dict.pop('_sa_instance_state', None)
    return jsonify(item_dict)


@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    item_list = []
    for item in items:
        item_dict = item.__dict__
        item_dict.pop('_sa_instance_state', None)
        item_list.append(item_dict)
    return jsonify(item_list)


@app.route('/items', methods=['POST'])
def create_item():
    body = request.get_json()
    new_item = Item(body['titulo'], body['conteudo'])
    db.session.add(new_item)
    db.session.commit()
    return "Item criado"

@app.route('/items/<id>', methods=['PUT'])
def update_item(id):
    body = request.get_json()
    item = Item.query.get(id)
    if item:
        item.titulo = body['titulo']
        item.conteudo = body['conteudo']
        db.session.commit()
        return "Item atualizado"
    return "Item não encontrado", 404

@app.route('/items/<id>', methods=['DELETE'])
def delete_item(id):
    item = Item.query.get(id)
    if item:
        db.session.delete(item)
        db.session.commit()
        return "Item apagado"
    return "Item não encontrado", 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
