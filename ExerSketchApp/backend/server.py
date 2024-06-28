from flask import Flask, request
from flask_cors import CORS
import json 
import os

UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})


def get_file():
    with open("../data/scores.json", "r") as file:
        return json.load(file)
    
def update_file(new_data):
    with open("../data/scores.json", "w") as file:
        json.dump(new_data, file)

@app.route("/activities", methods=["GET"])
def activities():
    saved_files = os.listdir(UPLOAD_FOLDER)
    result = []
    for i in range(len(saved_files)):
        result.append({"id": i, "score": saved_files[i]})

    return result



@app.route("/fileupload", methods=["GET", "POST"])
def fileupload():
    if request.method == "POST":
        file = request.files["file"]
        filename = request.form.get("title")
        file.save("uploads/" + filename + ".gpx")
        return "file saved!", 200


if __name__ == "__main__":
    app.run(host = "192.168.0.38", debug=True)