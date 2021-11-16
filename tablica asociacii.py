from sqlalchemy import column, Integer, String, table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column

from models.database import base

association_table = table ('association', base.metadata,
                           column('leson_id', Integer, ForeignKey('lesons.id))'
                           column('programisti_id', Integer, ForeignKey('programistiid'))
                           )
                                  