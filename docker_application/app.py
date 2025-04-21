from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_docker():
    return "<h1>welcome docker virtual environment!</h1>"


if __name__ == "__main__":
    app.run(debug=True)