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
        name = request.form.get("name")
        title = request.form.get("title")
        details = request.form.get("details")
        labels = request.form.getlist("labels[]")

        body = f"Issue reported by {name}\n\nDetails:\n{details}\n\nLabels: {', '.join(labels)}"

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

    return render_template_string("""
      <h2>Submit an Issue</h2>
      <form method="POST">
        <label>Your Name</label><br>
        <input type="text" name="name" required><br><br>

        <label>Issue Title</label><br>
        <input type="text" name="title" required><br><br>

        <label>Issue Details</label><br>
        <textarea name="details" rows="5" required></textarea><br><br>

        <label>Labels</label><br>
        <select name="labels[]" multiple>
          <option value="Room">Room</option>
          <option value="Workshop">Workshop</option>
          <option value="Laser Cutter">Laser Cutter</option>
          <option value="Network">Network</option>
        </select><br><br>

        <button type="submit">Submit Issue</button>
      </form>
    """)




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
