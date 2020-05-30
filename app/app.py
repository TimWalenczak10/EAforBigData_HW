from flask import Flask, render_template
import requests
import json

def get_names():
    response = requests.get("http://api.open-notify.org/astros.json")
    data = json.loads(response.text)
    names = []
    for i in data['people']:
        names.append(i['name'])
    return names

app = Flask(__name__)

@app.route('/')
def Astronauts():
    mytitle = "These people are in space right now: "
    names = get_names()
    return render_template('Astronauts.html', title = mytitle, content = names)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
