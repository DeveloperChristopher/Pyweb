from flask import Flask, render_template, request, redirect, flash, session
from project import Project
from user import User

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

def authenticate_user(username, password):
    user = User()
    user_data = user.read_username(username)
    if len(user_data) == 0:
        flash("Username or password is incorrect")
        return redirect("/login")
    else:
        if user_data[0][2] == password:
            session["user_id"] = user_data[0][0]
            return redirect("/")
        else:
            flash("Username or password is incorrect")
            return redirect("/login")

@app.route("/authenticate", methods=['POST'])
def authenticate():
    form_data = request.form
    return authenticate_user(form_data["username"], form_data["password"])
    
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == '__main__':
    app.run()
