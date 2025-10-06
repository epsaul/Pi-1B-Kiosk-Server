from flask import Flask, request, render_template_string, send_from_directory
import requests
import os
from dotenv import load_dotenv

from datetime import datetime

def boot_log():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"🌄 [{timestamp}] Flask awakens. Listening for whispers in the morning light...")

boot_log()

# Load GitHub token from .env file
load_dotenv(dotenv_path="/home/ed/PiKiosk/.env")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# GitHub repo to submit issues to
REPO = "DoESLiverpool/somebody-should"


app = Flask(__name__, static_folder='static')

@app.route("/", methods=["GET", "POST"])
def submit_issue():
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        headers = {"Authorization": f"token {GITHUB_TOKEN}"}
        data = {"title": title, "body": body}
        response = requests.post(
            f"https://api.github.com/repos/{REPO}/issues",
            json=data,
            headers=headers
        )
        if response.status_code == 201:
            return "✅ Issue submitted!"
        else:
            return f"❌ Error: {response.status_code}<br>{response.text}"
    return send_from_directory('static', 'issueForm.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
