# Imported libraries
from flask import Flask, Response, render_template, request, jsonify
import json

# List of words (constant)
WORDS = tuple(json.load(open("static/data/words.json")))

# Flask app
app = Flask(__name__)


# Index endpoint (with search engine)
@app.route("/", methods=["GET"])
def index():
    search = request.args.get("search", "").lower()

    # If a search is done, return the words that match the search results
    if search:
        return Response(
            json.dumps([word for word in WORDS if search in word], indent=2),
            mimetype="application/json",
            headers={"Content-Disposition": "attachment;filename=results.json"}
        )

    # If no search is done, render the HTML page    
    return render_template("index.html")


# Download endpoint (returns the list of words)
@app.route("/download", methods=["GET"])
def download():
    return Response(
        json.dumps(WORDS, indent=2),
        mimetype="application/json",
        headers={"Content-Disposition": "attachment;filename=results.json"}
    )


# API endpoint (with search parameters)
@app.route("/api", methods=["GET"])
def api():
    search = request.args.get("search", "").lower()

    # If a search is done, return the words that match the search results
    if search:
        return jsonify([word for word in WORDS if search in word])
       
    # If no search is done, return the complete list of words
    return jsonify(WORDS)


# Executes the program
if __name__ == "__main__":
    app.run(debug=True)