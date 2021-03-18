from flask import Flask

app = Flask("microblog")


#teste comentario
@app.route("/")
def index():
    return "Hello World"

app.run()