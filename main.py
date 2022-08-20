from flask import Flask,request,send_from_directory,render_template
from flask_cors import CORS
from FormHandler import FormHandler

app = Flask(__name__,static_folder='build/static',template_folder='build')
CORS(app)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/data',methods=['POST'])
def submit():
    data = request.json
    filename = FormHandler().generate(data)
    print(filename)
    return "200"

if __name__ == '__main__':
    app.run(debug=True)


