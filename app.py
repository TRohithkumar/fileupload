import os
from flask import Flask, request, render_template, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER= 'C:\Users\Rohith Tulla\Desktop\uploadfolder'
ALLOWED_EXTENSION= (['gif', 'jpg', 'jpeg','docx', 'png', 'txt'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/'  )
def hello_world():
    return render_template('home.html')


@app.route('/uploads', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in requested.files:
            flash('no file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('no file selected')
            return redirect(request.url)
        if file and allowed.file(file.filename):
            filename = secure_filename(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file'),filename=filename)
        return ...


if __name__ == '__main__':
    app.run(debug=true)
