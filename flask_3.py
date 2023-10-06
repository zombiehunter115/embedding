from flask import Flask
app= Flask(__name__)
@app.route("/")
def second_flask():
    return "this is my first flask program"

@app.route("/flask_3")
def third_flask():
    return "I love swimming!"

app.run()