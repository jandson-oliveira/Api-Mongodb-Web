from flask import Flask, request, jsonify, send_file # type: ignore
from flask_pymongo import PyMongo # type: ignore
from bson.objectid import ObjectId # type: ignore
import gridfs # type: ignore
from io import BytesIO
import os

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

# Rota para a home
@app.route('/')
def home():
    return "API rodando com sucesso!"

# Conexão com o MongoDB e GridFS
mongo = PyMongo(app)
fs = gridfs.GridFS(mongo.db)

# Rota para upload de arquivos
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    file_id = fs.put(file, filename=file.filename, content_type=file.content_type)
    
    return jsonify({
        "status": "ok",
        "id": str(file_id),
        "filename": file.filename
    })

# Rota para listar arquivos
@app.route('/files', methods=['GET'])
def list_files():
    files = []
    for f in fs.find().sort("uploadDate", -1):
        files.append({
            "id": str(f._id),
            "filename": f.filename,
            "uploadDate": f.upload_date.isoformat(),
            "size": f.length
        })
    return jsonify(files)

# Rota para download de arquivos
@app.route('/download/<file_id>', methods=['GET'])
def download_file(file_id):
    try:
        file = fs.get(ObjectId(file_id))
        return send_file(BytesIO(file.read()), download_name=file.filename, mimetype=file.content_type)
    except:
        return jsonify({"error": "File not found"}), 404

# Inicia o servidor Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
