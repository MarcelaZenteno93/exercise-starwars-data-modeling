import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    email= Column(String(250) ,nullable=False)

    favorites = relationship('Favorite', back_populates='user')

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(100))
    terrain = Column(String(100))

    favorites = relationship('Favorite', back_populates='planet')

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer,primary_key=True)
    name = Column(String(100), nullable=False)
    birth_year = Column(String(20))
    gender = Column(String(20))

    favorites = relationship('Favorite', back_populates='character')

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id=Column(Integer, ForeignKey('user.id'),nullable=False)
    planet_id=Column(Integer, ForeignKey('planet.id'))
    character_id=Column(Integer, ForeignKey('character_id'))
    timestamp= Column(DateTime(timezone=True),server_default=func.now())

    user = relationship(User, back_populates='favorites')
    planet = relationship(Planet, back_populates='favorites')
    character = relationship(Character,  back_populates='favorites')


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
