from sqlalchemy import column, Integer, String,  ForeignKey
from sqlalchemy.sql.expression import true 

from models.database import base

class programisti(base):
    __tablename__ ='programisti'
    
    id = column (Integer, prymary_key=true)
    surname = column (String)
    name = column (String)
    patronymic = column(String) 
    age = column (Integer)
    
def __init__(self, full_name: list[str], age) :
    self. surname = full_name[0]
    self.name = full_name[1]
    self.patronymic = full_name[2]
    self.age = age
     
    