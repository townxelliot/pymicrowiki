# file location of the sqlite db
import os

_base_path = os.path.join(os.path.dirname(__file__), '..', 'STORAGE')
os.makedirs(_base_path, exist_ok=True)

def _build_path(path_segment):
    return os.path.abspath(os.path.join(_base_path, path_segment))

config = {
    'sqlite_uri': 'sqlite:///' + _build_path('db.sqlite'),
    'file_folder': _build_path('files'),
}
