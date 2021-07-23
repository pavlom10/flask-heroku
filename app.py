import os
import re
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

uri = os.getenv("DATABASE_URL")  # or other relevant config var
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
# rest of connection code using the connection string `uri`

app.config['SQLALCHEMY_DATABASE_URI'] = uri
db = SQLAlchemy(app)
