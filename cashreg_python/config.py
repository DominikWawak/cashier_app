import os
class Config:
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{os.environ['DB_USERNAME']}:{os.environ['DB_PASSWORD']}@{os.environ['MYSQL_DB_URL']}/sensordatadb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
