from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world from edvilme!!"

@app.route("/test")
def test():
    return "This is a test"

if __name__ == "__main__":
    app.run(port=3000)