from sqlalchemy import Column, Integer, String
from database.database import db

class Pedidos(db.Model):
  __tablename__ = 'pedidos'

  id = Column(Integer, primary_key=True, autoincrement=True)
  nome = Column(String(50), nullable=False)
  email = Column(String(50), nullable=False)
  descricao = Column(String(50), nullable=False)

  def __repr__(self):
    return f'<Pedidos:[id:{self.id}, nome:{self.nome}, email:{self.email}, descricao:{self.descricao}]>'
  
  def serialize(self):
    return {
      "id": self.id,
      "nome": self.nome,
      "email": self.email,
      "descricao": self.descricao}