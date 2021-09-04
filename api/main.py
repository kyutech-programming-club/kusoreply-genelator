from flask import Flask, request

from generator import gen_reply
# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    """ Return a friendly HTTP greeting. """
    return "Hello World!. Deploy from github actions\n"

@app.route("/gen_reply", methods=["GET", "POST"])
def gen_reply():
    if request.method == "GET":
        return "Please send the text you want to generate a fucking lip\n"
    else :
        try:
            input_text = request.form('input')
        except KeyError:
            input_text = "Input is must not be blank"

        reply = gen_reply(input_text)
        return reply

if __name__ == "__main__":
    # Used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host="localhost", port=8080, debug=True)
