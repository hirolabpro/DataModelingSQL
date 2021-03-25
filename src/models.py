import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

#Parent
class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    diameter = Column(Integer)
    climate = Column(String(20))
    gravity = Column(String(40))
    terrain = Column(String(50))
    surface_water = Column(Integer)
    population = Column(Integer)
    climate = Column(String(50))
    created = Column(String(50))
    edited = Column(String(50))
    url = Column(String(100))


    def to_dict(self):
        return {}

   #{
	#"name": "Yavin IV",
	#"rotation_period": "24",
	#"orbital_period": "4818",
	#"diameter": "10200",
	#"climate": "temperate, tropical",
	#"gravity": "1 standard",
	#"terrain": "jungle, rainforests",
	#"surface_water": "8",
	#"population": "1000",
	#"residents": [],
	#"films": [
		#"http://swapi.dev/api/films/1/"
	#],
	#"created": "2014-12-10T11:37:19.144000Z",
	#"edited": "2014-12-20T20:58:18.421000Z",
	#"url": "http://swapi.dev/api/planets/3/"
#}

#Child
class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(20))
    skin_color = Column(String(20))
    eye_color = Column(String(10))
    birth_year = Column(Date, nullable=False)
    gender = Column(String(15))
    homeworld = Column(String(50), ForeignKey(Planet.name))
    films = Column(String(250))

    def to_dict(self):
        return {}

    #"name": "Luke Skywalker",
	#""height": "172",
	#""mass": "77",
	#""hair_color": "blond",
	#""skin_color": "fair",
	#""eye_color": "blue",
	#""birth_year": "19BBY",
	#""gender": "male",
	#""homeworld": "https://swapi.dev/api/planets/1/",
	#""films": [
		#""https://swapi.dev/api/films/2/",
		#""https://swapi.dev/api/films/6/",
		#""https://swapi.dev/api/films/3/",
		#""https://swapi.dev/api/films/1/",
		#""https://swapi.dev/api/films/7/"
	#"],


class StartShip(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    model = Column(String(25))
    manufacturer = Column(String(100))
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    max_atmosphering_speed = Column(String(40))
    crew = Column(Integer)
    passengers = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String(40))
    hyperdrive_rating = Column(Integer)
    MGLT = Column(Integer)
    starship_class = Column(String(40))
    films = Column(String(250))
    created = Column(String(80))
    edited = Column(String(80))
    url = Column(String(80))

    def to_dict(self):
        return {}

#{
	#"name": "Death Star",
	#"model": "DS-1 Orbital Battle Station",
	#"manufacturer": "Imperial Department of Military Research, Sienar Fleet Systems",
	#"cost_in_credits": "1000000000000",
	#"length": "120000",
	#"max_atmosphering_speed": "n/a",
	#"crew": "342,953",
	#"passengers": "843,342",
	#"cargo_capacity": "1000000000000",
	#"consumables": "3 years",
	#"hyperdrive_rating": "4.0",
	#"MGLT": "10",
	#"starship_class": "Deep Space Mobile Battlestation",
	#"pilots": [],
	#"films": [
		#"http://swapi.dev/api/films/1/"
	#],
	#"created": "2014-12-10T16:36:50.509000Z",
	#"edited": "2014-12-20T21:26:24.783000Z",
	#"url": "http://swapi.dev/api/starships/9/"
#}


class Username(Base):
    __tablename__ = 'username'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)


    def to_dict(self):
        return {}

class Favorites(Base):
    __tablename__ = 'favorites'
    user_id = Column(Integer, ForeignKey(Username.id))
    id = Column(Integer, primary_key=True)
    name = Column(String(60))
    planet_name = Column(String(60), ForeignKey(Planet.name))
    person_name = Column(String(60), ForeignKey(Character.name))
    startship = Column(String(60), ForeignKey(StartShip.name))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')