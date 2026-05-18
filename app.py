from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template("pages/home.html")

@app.route('/projects')
def projects():  # put application's code here
    return render_template("pages/projects/index.html", projects=
                           [
                               ["111111111", "Project 1", "Description of project 1"],
                               ["222222222", "Project 2", "Description of project 2"],
                               ["333333333", "Project 3", "Description of project 3"],
                               ["444444444", "Project 4", "Description of project 4"]
                           ])


if __name__ == '__main__':
    app.run()
