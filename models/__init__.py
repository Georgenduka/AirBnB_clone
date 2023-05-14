#!/usr/bin/python3
"""create a unique FileStorage instance for the application"""
from models.engine.file_storage import FileStorage
import json

storage = FileStorage()
storage.reload()
