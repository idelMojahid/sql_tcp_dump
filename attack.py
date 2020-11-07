from sqlalchemy import Column, Integer, String
from base import Base
import json


class Attack(Base):
    __tablename__ = 'attacks'

    id = Column(Integer, primary_key=True)
    host = Column(String(20))
    port = Column(String(20))

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def toJSON(self):
        return json.dumps({"id": self.id, "host": self.host, "port": self.host})
