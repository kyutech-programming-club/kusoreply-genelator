from flask import Flask, request
from flask_cors import CORS
import nltk

from generator import gen_reply

nltk.data.path.append("api/nltk_data")

app = Flask(__name__)

HEADERS= {
    "Access-Control-Allow-Origin": "*",
}
CORS(app)

@app.route("/", methods=["GET", "POST"])
def reply():
    if request.method == "GET":
        return ("Hello World!. Deploy from github actions\n", 200, HEADERS)
    else :
        try:
            input_text = request.json["input"]
        except KeyError:
            return ("Input is must not be blank", 400, HEADERS)

        reply = gen_reply(input_text)
        return (reply, 200, HEADERS)

if __name__ == "__main__":
    # Used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host="localhost", port=8080, debug=True)
