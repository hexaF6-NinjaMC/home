import os

from english_dictionary import printRandWord

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def main():
    # name = os.environ.get("NAME", "dear user")
    # return f'Hello, {name}! {printRandWord()}'
    return render_template('blog-home.html')

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

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
