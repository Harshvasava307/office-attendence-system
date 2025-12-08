import os

class FileService:
    def file_exists(self, path):
        return os.path.isfile(path)
