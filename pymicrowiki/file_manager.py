import os

from flask import g
from werkzeug.utils import secure_filename

from pymicrowiki import config


class FileManager:

    def __init__(self, file_folder):
        self.file_folder = file_folder
        if not os.path.isdir(file_folder):
            os.makedirs(file_folder, exist_ok=True)

    def _get_path(self, file_name):
        return os.path.join(self.file_folder, file_name)

    def list(self):
        return sorted(os.listdir(self.file_folder))

    def add(self, uploaded):
        # uploaded is a file from the request.files array
        secure_path = self._get_path(secure_filename(uploaded.filename))
        uploaded.save(secure_path)
        return True

    def delete(self, file_name):
        os.remove(self._get_path(file_name))
        return True

    def get_path(self, file_name):
        return os.path.join(self.file_folder, file_name)


def get_fm():
    if 'fm' not in g:
        g.fm = FileManager(config['file_folder'])
    return g.fm
