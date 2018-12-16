import os


class FileInfo:
    def __init__(self, path):
        self.original_path = path
        self.filename = os.path.basename(path)
