# Imported libraries
from flask import Flask, render_template, request, jsonify, Response
import json

# List of words (constant)
WORDS = tuple(json.load(open("words.json")))

# Flask app
app = Flask(__name__)


# API endpoint (with search parameters)
@app.route("/api", methods=["GET"])
def api():
    search = request.args.get("search")

    # If a search is done, return the words that match the search results
    if search:
        return jsonify([word for word in WORDS if search in word])
    
    return jsonify(WORDS)


# Home endpoint (with search engine)
@app.route("/", methods=["GET"])
def home():
    search = request.args.get("search")

    # If a search is done, return the words that match the search results
    if search:
        return Response(
            json.dumps([word for word in WORDS if search in word], indent=2),
            mimetype="application/json",
            headers={"Content-Disposition": "attachment;filename=results.json"}
        )
    
    return render_template("home.html")


# Download endpoint (returns the list of words)
@app.route("/download", methods=["GET"])
def download():
    return Response(
        json.dumps(WORDS, indent=2),
        mimetype="application/json",
        headers={"Content-Disposition": "attachment;filename=results.json"}
    )


# Executes the program
if __name__ == "__main__":
    app.run(debug=True)