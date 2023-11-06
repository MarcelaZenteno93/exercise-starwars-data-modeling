import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    email = Column(String(250), nullable=False)

    favorite = relationship('Favorite', back_populates='user')

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(100))
    terrain = Column(String(100))

    favorite = relationship('Favorite', back_populates='planet')

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    birth_year = Column(String(20))
    gender = Column(String(20))

    favorite = relationship('Favorite', back_populates='character')

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship('User', back_populates='favorite')
    planet = relationship('Planet', back_populates='favorite')
    character = relationship('Character', back_populates='favorite')

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
