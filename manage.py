import os

from flask import Flask
from flask.ext.script import Manager, Command
from flask.ext.thumbnails import Thumbnail


UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/img/project_thumbs')
PROJECT_IMAGE_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/img/projects')

app = Flask(__name__)
app.config.from_object(__name__)
manager = Manager(app)
thumb = Thumbnail(app)


class CreateThumbnails(Command):
    def run(self):
        print('Create thumbnails')
        for f in os.listdir(PROJECT_IMAGE_FOLDER):
            filepath = os.path.join(PROJECT_IMAGE_FOLDER, f)
            if os.path.isfile(filepath):
                print('Creating thumbnail for %s' % f)
                thumb.thumbnail(filepath, '370x197', crop='fit')
                thumb.thumbnail(filepath, '24x24', crop='fit')

if __name__ == '__main__':
    manager.add_command('create_thumbnails', CreateThumbnails())
    manager.run()
