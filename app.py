"""
Accessible Gamified Quiz System
================================
Main Flask application file.
Run this file to start the web server.
"""

from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime
from questions import QUESTIONS

# ── Create the Flask app ──────────────────────────────────────
app = Flask(__name__)

# File where all student scores will be saved
SCORES_FILE = "scores.json"

# Teacher credentials (you can change these)
TEACHER_USERNAME = "teacher"
TEACHER_PASSWORD = "teacher123"


# ── Helper functions ──────────────────────────────────────────

def load_scores():
    """Load all scores from the JSON file."""
    if not os.path.exists(SCORES_FILE):
        return []
    with open(SCORES_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_scores(scores):
    """Save all scores to the JSON file."""
    with open(SCORES_FILE, "w") as f:
        json.dump(scores, f, indent=2)


# ── Routes ────────────────────────────────────────────────────

@app.route("/")
def home():
    """Serve the main quiz page, passing questions to the template."""
    return render_template("index.html", questions=QUESTIONS)


@app.route("/api/login/teacher", methods=["POST"])
def teacher_login():
    """Check teacher username and password."""
    data = request.get_json()
    username = data.get("username", "").strip()
    password = data.get("password", "")

    if username == TEACHER_USERNAME and password == TEACHER_PASSWORD:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False, "message": "Incorrect username or password."})


@app.route("/api/scores", methods=["GET"])
def get_scores():
    """Return all saved student scores."""
    scores = load_scores()
    return jsonify(scores)


@app.route("/api/scores", methods=["POST"])
def save_score():
    """Save a new student score after completing a quiz."""
    data = request.get_json()

    # Build the score record
    record = {
        "name":       data.get("name", "Unknown"),
        "section":    data.get("section", ""),
        "subject":    data.get("subject", ""),
        "difficulty": data.get("difficulty", "easy"),
        "score":      data.get("score", 0),
        "bestStreak": data.get("bestStreak", 0),
        "date":       datetime.now().isoformat()
    }

    scores = load_scores()
    scores.append(record)
    save_scores(scores)

    return jsonify({"success": True, "record": record})


@app.route("/api/scores", methods=["DELETE"])
def clear_scores():
    """Delete all student scores (teacher only)."""
    save_scores([])
    return jsonify({"success": True, "message": "All records cleared."})


# ── Start the server ──────────────────────────────────────────

#if __name__ == "__main__":
    #print("=" * 50)
    #print("  Accessible Gamified Quiz System")
    #print("  Running at: http://127.0.0.1:5000")
    #print("  Press CTRL+C to stop the server")
    #print("=" * 50)
    #app.run(debug=True)
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
