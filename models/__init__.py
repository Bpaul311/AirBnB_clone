#!/usr/bin/python3
"inits files for the models's package"

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
