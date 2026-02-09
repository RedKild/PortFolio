from flask import Blueprint, app, request, jsonify
from models import db, Doc

docs_bp = Blueprint('docs', __name__)

@docs_bp.route('/api/docs', methods=['POST'])
def create_doc():
    data = request.get_json()

    # Vérif basique
    if not data or 'title' not in data or 'description' not in data:
        return jsonify({"error": "title et description requis"}), 400

    # Évite doublon description (car unique=True)
    if Doc.query.filter_by(description=data['description']).first():
        return jsonify({"error": "Description déjà utilisée"}), 409

    new_doc = Doc(
        title=data['title'],
        description=data['description']
    )

    db.session.add(new_doc)
    db.session.commit()

    return jsonify({
        "message": "Doc créé",
        "doc": {
            "id": new_doc.id,
            "title": new_doc.title,
            "description": new_doc.description
        }
    }), 201

@docs_bp.route('/api/docs', methods=['GET'])
def get_docs():
    docs = Doc.query.all()

    result = []
    for d in docs:
        result.append({
            "id": d.id,
            "title": d.title,
            "description": d.description
        })

    return jsonify(result), 200