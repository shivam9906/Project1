from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from ECS! 🚀"

def home2():
    return "Hello from TESTING! "

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)