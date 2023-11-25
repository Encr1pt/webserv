from flask import Flask

app = Flask(__name__)

#public ip: 81.107.232.9


@app.route('/')
def hello():
    return 'Hello, jack'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port='5000',debug=True)
