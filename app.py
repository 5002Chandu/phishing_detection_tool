from flask import Flask, render_template, request
import re
from urllib.parse import urlparse

app = Flask(__name__)

def check_phishing(url):
    score = 0

    # URL length check
    if len(url) > 75:
        score += 1

    # @ symbol check
    if "@" in url:
        score += 1

    # IP address check
    ip_pattern = r"(\d{1,3}\.){3}\d{1,3}"
    if re.search(ip_pattern, url):
        score += 1

    # HTTPS check
    if not url.startswith("https"):
        score += 1

    # Hyphen in domain
    domain = urlparse(url).netloc
    if "-" in domain:
        score += 1

    if score >= 2:
        return "⚠️ This website may be a PHISHING site."
    else:
        return "✅ This website looks SAFE."

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        url = request.form["url"]
        result = check_phishing(url)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)