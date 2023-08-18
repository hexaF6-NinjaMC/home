import sys
import os
sys.path.append("example_youtube")

from english_dictionary import printRandWord

from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    name = os.environ.get("NAME", "dear user")
    return f'Hello, {name}! {printRandWord()}'

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
