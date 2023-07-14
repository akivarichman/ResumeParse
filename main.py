# https://www.youtube.com/watch?v=GeiUTkSAJPs
# https://www.youtube.com/watch?v=I9BBGulrOmo
from flask import Flask, flash, request, redirect, url_for, render_template # render_template allows us to return actual files instead of just text
from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
import re


app = Flask(__name__) # an instance of a Flask web application
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


class UploadFileForm(FlaskForm):
    files = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")


ALLOWED_EXTENSIONS = set(['txt'])


class Resumes:
    key_word_list = []
    def __init__(self, name):
        self.name = name
        self.master_word_list = []
        self.keywords = []
        self.score = 0
    def reset(self):
        self.master_word_list = []
        self.keywords = []
        self.score = 0


resumes = []


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS


def check(key_word, master_word_list):
    for i in range(len(master_word_list)):
        if key_word.lower() == master_word_list[i].lower():
            return True
    return False


@app.route("/", methods=['GET',"POST"]) # define how to access the page
@app.route("/home", methods=['GET',"POST"])
def home():
    form = UploadFileForm()
    if request.method == "POST":
        keys = request.form["keys"]
        Resumes.keyword_list = re.split('[^a-zA-Z0-9]', keys)
        if form.validate_on_submit():
            files = request.files.getlist('files')
            print('Hello', files)
            for file in files:
                filename = secure_filename(file.filename)
                # absolutePath = os.path.abspath(file.filename)
                if allowed_file(file.filename):
                    if not any(obj.name == filename for obj in resumes):
                        obj = Resumes(filename)
                        resumes.append(obj)
                    file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],filename)) # save the file           
                    
                else:
                    flash("Invalid File: only .txt files are allowed")
                    return redirect(request.url)
            return redirect(url_for('display_content', keys=keys))
    else:
        return render_template('index.html', form=form)


@app.route('/content/<keys>', methods=['GET',"POST"])
def display_content(keys):
    for resume in resumes:
        resume.reset()
        file = open(resume.name,'r')
        line = file.readline()
        while line:
            words = re.split('[^a-zA-Z0-9]', line)
            words = ' '.join(words).split()
            for i in range(len(words)):
                resume.master_word_list.append(words[i])
            line = file.readline()
        file.close()

        for i in range(len(Resumes.keyword_list)):
            is_there = check(Resumes.keyword_list[i], resume.master_word_list)
            if is_there:
                resume.keywords.append(Resumes.keyword_list[i])
                resume.score += 1

    resumes_sorted = sorted(resumes, key=lambda x: x.score, reverse=True)

    return render_template('content.html', resumes=resumes_sorted)


if __name__ == "__main__":
    app.run(debug=True)