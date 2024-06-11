import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.file_reader import read_file
from utils.code_writer import generate_code
from utils.code_executor import execute_code

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "/tmp"  # You can change this to any directory you prefer
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure the upload folder exists


@app.route("/generate-code", methods=["POST"])
def generate_code_route():
    data = request.get_json()
    file_content = data.get("fileContent")
    prompt = data.get("prompt")

    if not file_content or not prompt:
        return jsonify({"error": "File content and prompt are required."}), 400

    code = generate_code(file_content, prompt)
    if not code:
        return jsonify({"code": "", "output": "Failed to generate code."})

    result = execute_code(code)
    if result is None:
        return jsonify({"code": code, "output": "Failed to execute code."})

    return jsonify({"code": code, "output": result})


@app.route("/upload-file", methods=["POST"])
def upload_file():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file part in the request"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    try:
        file.save(file_path)
    except Exception as e:
        return jsonify({"error": f"Failed to save file: {str(e)}"}), 500

    file_content = read_file(file_path)
    if not file_content:
        return jsonify({"error": f"Failed to read file: {file.filename}"}), 500

    return jsonify({"fileContent": file_content})


if __name__ == "__main__":
    app.run(debug=True)
