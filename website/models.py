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
    conta = db.relationship('Conta')

class Conta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    saldo = db.Column(db.String)

admin.add_view(ModelView(Usuario, db.session))