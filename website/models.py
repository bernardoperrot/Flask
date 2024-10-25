from . import db
from sqlalchemy.sql import func
from flask_login import UserMixin
from flask_admin.contrib.sqla import ModelView
from . import admin


class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    senha = db.Column(db.String(150))
    nome = db.Column(db.String(150))
    pessoas = db.relationship('Pessoas')

class Pessoas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    nome = db.Column(db.String)
    idade = db.Column(db.Integer)

admin.add_view(ModelView(Usuario, db.session))