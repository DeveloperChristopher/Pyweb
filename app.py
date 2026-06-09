import os
from flask import Flask, render_template, request, redirect, flash, session
from project import Project
from user import User

UPLOAD_FOLDER_IMG = "/static/img/projects"
UPLOAD_FOLDER_PROJECTS = "/static/projects"

app = Flask(__name__)
app.secret_key = "asohdj asoxcvncxvmn"
    

@app.route('/')
def index():
    return render_template("pages/home.html")


def get_projects_db():
    project = Project()
    return project.read_all()


@app.route('/projects', methods=['GET'])
def projects():
    return render_template("pages/projects/index.html", projects=get_projects_db())


@app.route('/create/project')
def create_project():
    return render_template("pages/projects/create.html")


def store_project_db(title, body, img_type):
    project = Project()
    return project.create(title, body, img_type)

# Deze functie is gemaakt met AI
def get_image_type(file_data):
    return file_data.content_type.split("/")[1]


@app.route('/store/project', methods=['POST'])
def store_project():
    if request.method == 'POST':
        form_data = request.form
        try:
            file_type = get_image_type(request.files["image"])
            project_id = store_project_db(form_data["title"], form_data["body"], file_type)
            request.files["image"].save(f"static/img/projects/{project_id}.{file_type}")
            request.files["project"].save(f"static/projects/{project_id}.zip")
        except:
            print("Failed to store project")
        return redirect("/projects")
    else:
        return redirect("/")


def get_project_db(id):
    project = Project()
    return project.read_id(id)


def edit_project_db(id, columns, values):
    project = Project()
    project.update(id, columns, values)


@app.route('/edit/project', methods=['POST'])
def edit_project():
    if request.method == 'POST':
        form_data = request.form
        edit_project_db(form_data["id"], ["title", "body"], [form_data["title"], form_data["body"]])
        return redirect("/projects")
    else:
        redirect("/")


@app.route('/update/project', methods=['GET'])
def update_project():
    form_data = request.args
    return render_template("pages/projects/update.html", project=get_project_db(form_data["id"]))


def delete_project_db(id):
    project = Project()
    project.delete_id(id)


@app.route('/delete/project', methods=['GET'])
def delete_project():
    form_data = request.args
    try:
        os.remove(f"static/img/projects/{form_data["id"]}.{ get_project_db(form_data['id'])[0][3] } ")
        os.remove(f"static/projects/{form_data["id"]}.zip")
        delete_project_db(form_data["id"])
    except:
        print("Failed to delete")
    return redirect("/projects")


@app.route('/project', methods=['GET'])
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
    if request.method == 'POST':
        form_data = request.form
        return authenticate_user(form_data["username"], form_data["password"])
    else:
        redirect("/")
    

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == '__main__':
    app.run()
