from flask import Flask, render_template, request, redirect
from project import Project

app = Flask(__name__)
app.secret_key = "asohdj asoxcvncxvmn"

@app.route('/')
def index():
    return render_template("pages/home.html")

def get_projects_db():
    project = Project()
    return project.read_all()

@app.route('/projects', methods=['GET', 'POST'])
def projects():
    return render_template("pages/projects/index.html", projects=get_projects_db())

def get_project_db(id):
    project = Project()
    return project.read_id(id)

@app.route('/project')
def project():
    form_data = request.args
    return render_template("pages/projects/show.html", project=get_project_db(form_data["id"]))

@app.route('/contact', methods=['GET', 'POST'])
def contact(): 
    form_data = request.form
    page = "form" # put application's code here
    if request.method == 'POST':
        page = "data"
    return render_template("pages/contact.html", page=page, form_data=form_data)

@app.route('/login')
def login(): 
    return render_template("pages/users/login.html")

@app.route("/authenticate", methods=['POST'])
def authenticate():
    form_data = request.form
    print(form_data["password"])
    return redirect("/")
    

if __name__ == '__main__':
    app.run()
