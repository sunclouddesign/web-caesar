from flask import Flask
from caesar import rotate_string
from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True
form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form action="/rotate" method="post">
          <label for="rot">Rotate by:</label>
          <input type="text" name="rot" id="rot" value="0"><br>
          <textarea name="text" value="">{0}</textarea><br>
          <input type="submit" value="Submit">
      </form>
    </body>
</html>
"""
@app.route("/")
def index():
    return form.format("")

@app.route('/rotate', methods = ['POST'])
def encrypt():
    rotated_text = rotate_string(str(request.form['text']),int(request.form['rot']))
    print(rotated_text)
    return form.format(rotated_text)


app.run()