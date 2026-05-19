from flask import Flask, render_template, request

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
