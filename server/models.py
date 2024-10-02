from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Column, String, Integer, Float
from sqlalchemy_serializer import SerializerMixin


metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# Add models here
class Earthquake(db.Model, SerializerMixin):
    __tablename__ = 'earthquakes'

    id = Column(Integer, primary_key=True)
    magnitude = Column(Float, nullable=False)
    location = Column(String, nullable=False)
    year = Column(Integer, nullable=False)

    def __repr__(self):
        return f'<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>'