from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template("pages/home.html")

@app.route('/projects')
def projects():  # put application's code here
    return render_template("pages/projects/index.html", projects=
                           [
                               ["111111111", "BPGRU", "Description of project 1"],
                               ["222222222", "BPYT1", "Description of project 2"],
                               ["333333333", "Project: Introductie", "Description of project 3"],
                               ["444444444", "BPGAA", "Description of project 4"]
                           ])


@app.route('/contact')
def contact():  # put application's code here
    return render_template("pages/contact.html")

if __name__ == '__main__':
    app.run()
