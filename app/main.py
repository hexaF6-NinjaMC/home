import os

from english_dictionary import printRandWord
from jinja2 import Template
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def main():
    name = os.environ.get("NAME", "dear viewer")
    random_word = f'Hello, {name}! {printRandWord()}'
    return render_template('blog-home.html', randomWord = random_word)

@app.route('/blogs/<template>')
def post_blog(template):
    return render_template(f'/blogs/{template}')

@app.route('/<dir>/<name>/<filename>')
def render_blog(dir, name, filename):
    name = request.query_string('name')
    file = request.files[f'/{dir}/{name}/{filename}']
    with open(file, 'r') as file:
        content = file.read()
        return content
    
# @app.route('/api', method = ['GET'])
# def get_queries():
#     ...

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
