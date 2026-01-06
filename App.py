from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/web")
def web():
    return send_from_directory("web", "index.html")

@app.route("/")
def home():
    return "Bot is running!"

if __name__ == "__main__":
    app.run()
