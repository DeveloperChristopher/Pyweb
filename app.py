from flask import Flask, render_template, request
from project import Project

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("pages/home.html")

@app.route('/projects')
def projects():
    project = Project()
    print(project.read_all())
    return render_template("pages/projects/index.html")

@app.route('/project')
def project():
    form_data = request.args
    return render_template("pages/projects/show.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact(): 
    form_data = request.form
    page = "form" # put application's code here
    if request.method == 'POST':
        page = "data"
    print(form_data)
    return render_template("pages/contact.html", page=page, form_data=form_data)

if __name__ == '__main__':
    app.run()
