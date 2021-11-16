from sqlalchemy import column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import true

from models.database import base

class programisti(base):
    __tablename__ = 'programisti'

    id = column(Integer, primary_kay=true)
    programisti_name = column(String)
    programisti =relationship('programisti')
    
    def __repr__(self):
        return f'програмисти [id: {self.id}, название: {self.programisti_name} ]'
    
    