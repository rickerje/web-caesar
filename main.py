from flask import Flask, request
from caesar import rotate_character
app = Flask(__name__)

app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <form method = "post">
        <label>Rotate by: 
        <input type = "text" name = "rot" value="0" />
        </label>
        <input type = "textarea" name = "text" />
        <input type = "submit" />
      </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    encrypted_string = ''

    for char in text:
        encrypted_string = encrypted_string + rotate_character(char, rot)

    return encrypted_string

app.run()
