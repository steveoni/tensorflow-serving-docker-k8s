from flask import Flask, render_template, flash, request
import requests
from os import environ

app = Flask(__name__)


def get_rest_request(text, model_name="model"):
    url = "http://server:8501/v1/models/{}:predict".format(model_name)
    payload = {"instances": [text]}
    response = requests.post(url=url, json=payload)
    return response

@app.route("/home",methods=["GET","POST"])
def home():

    if request.method == "POST":

        inp1 = int(request.form["inp1"])
        inp2 = int(request.form["inp2"])

        response = get_rest_request([inp1,inp2], "1597001936")

        resp = response.json()
        flash(f"obtained {inp1} and {inp2} have a prediction of {resp['predictions']}", 'success')

    return render_template("index.html")

app.secret_key = "nlhkjtgjhfhvhjfyfgcjgdtdgcngcghdt"
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(environ.get('PORT', 8080)))