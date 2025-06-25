from flask import Flask, render_template, request, jsonify
from rules_engine import evaluate_rules

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    data = request.json
    result, alerts = evaluate_rules(data)
    return jsonify({"result": result, "alerts": alerts})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)