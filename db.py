# -*- coding: utf-8 -*-

import psycopg2
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
import random


#engine = create_engine("postgresql+psycopg2://postgres:852258852@localhost/modul3")
engine = create_engine('sqlite:///my_language_helper.db',echo=False)
Base = declarative_base()

class Words(Base):

    __tablename__ = "language_helper"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    word = Column(String, nullable=False, unique=True)
    translate = Column(String, nullable=False)

Base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
s=Session()


def add_word(word, translate):
    new_word = Words(word=word, translate=translate)
    s.merge(new_word)
    s.commit()


def get_random_word():

    random_word = s.query(Words).all()
    return random.choice(random_word) if random_word else None