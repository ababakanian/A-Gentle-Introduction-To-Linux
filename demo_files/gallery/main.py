import os
from flask import Flask, request, session, g, \
    redirect, url_for, abort, \
    flash, render_template, escape

app = Flask(__name__)
app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(
	dict(
    IMAGE_PATH='/home/armen/gallery/static/photos'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


@app.route("/")
def gallery():

    image_list = []

    image_dir = os.listdir(app.config['IMAGE_PATH'])

    for image in image_dir:
        t_item = {
                  'src': url_for('static', filename="photos/{0}".format(image)),
                  'link': url_for('static', filename="photos/{0}".format(image))
                  }
        image_list.append(t_item)



    # construct the title
    return render_template("gallery_ninja.html",
                           images=image_list)


if __name__ == "__main__":
    app.run()
