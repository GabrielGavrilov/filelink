from db_settings import db

"""
	DATABASE MODELS
"""

# @MODEL: File Storage Model
# @DESCRIPTION: Creates and stores a file dataset onto a given folder.
class FileStorage(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	file = db.Column(db.Text, unique=True, nullable=False)
	file_name = db.Column(db.Text, nullable=False)
	file_mimetype = db.Column(db.Text, nullable=False)
	folder_destination = db.Column(db.Text, nullable=False)

# @MODEL: Folder Model
# @DESCRIPTION: Creates a folder dataset where the files are stored onto.
class FolderModel(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	folder_name = db.Column(db.Text, nullable=False)