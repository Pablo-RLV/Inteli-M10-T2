from sqlalchemy import Column, Integer, String
from database.database import db

class User(db.Model):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True, autoincrement=True)
  username = Column(String(50), nullable=False)
  password = Column(String(50), nullable=False)

  def __repr__(self):
    return f'<User:[id:{self.id}, username:{self.username}, password:{self.password}]>'
  
  def serialize(self):
    return {
      "id": self.id,
      "username": self.username,
      "password": self.password}
  
class Notes(db.Model):
  __tablename__ = 'notes'

  id = Column(Integer, primary_key=True, autoincrement=True)
  text = Column(String(50), nullable=False)

  def __repr__(self):
    return f'<Notes:[id:{self.id}, text:{self.text}]>'
  
  def serialize(self):
    return {
      "id": self.id,
      "text": self.text}