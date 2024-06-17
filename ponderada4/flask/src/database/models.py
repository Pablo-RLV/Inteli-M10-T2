from sqlalchemy import Column, Integer, String
from database.database import db
  
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