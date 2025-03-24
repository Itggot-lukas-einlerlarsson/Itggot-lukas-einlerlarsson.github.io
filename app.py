# import the Flask class from the flask module
from flask import Flask, render_template
from werkzeug.middleware.proxy_fix import ProxyFix
import os

# create the application object
app = Flask(__name__)

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

# use decorators to link the function to a url
@app.route('/')
def home():
    image_folder = os.path.join("static", "img")
    images = [f"img/{img}" for img in os.listdir(image_folder) if img.endswith((".png", ".jpg", ".jpeg", ".gif"))]
    return render_template('index.html', images=images)  # return a string

@app.errorhandler(404)
def page_not_found(e):
    # your processing here
    return render_template('index.html')

# start the server with the 'run()' method
if __name__ == '__main__':
    
    app.run(debug=True, port=8000) # NOTE
