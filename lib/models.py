from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from aux import getconfig
"""
models.py
Created by Anthony Velardi on 01-21-2017

poppin bottles fuckin models
"""
#TODO DONE: pull sql options from config once schema is confirmed

##Todo, global vs local table prefix handling function, return prefix

config = getconfig()


wlblconf = config['defaults']['wlbl']
shortsl = wlblconf['shortstrlen']
tablebase = config['basic']['db']['global']['tableprefix']


Base = declarative_base()

class Client(Base):
    __tablename__ = tablebase + 'client'
    id = Column(Integer, primary_key=True)
    updatetype =  Column(Integer,default=wlblconf['client']['defaults']['connectiontype'])
    host = Column(String,default=None)
    description = Column(String,default=None)
    #filetype = Column(Integer,default=slimeconf['upload']['type'])
    created = Column(DateTime,default=None)
    modified = Column(DateTime,default=None)

class IPAddress(Base):
    __tablename__ = tablebase + 'ipaddress'
    id = Column(Integer, primary_key=True)
    accessmode = Column(Integer,default=0)
    address = Column(String)
    def __repr__(self):
        return self.address

    #filetype = Column(Integer,default=wlblconf['upload']['text']['type'])
    #title = Column(String(shortsl),default=slimeconf['upload']['text']['title'],nullable=slimeconf['upload']['text']['allowblanktitle'])
    #body = Column(Text,nullable=False)#dont allow blank notes
    #uploadid = Column(Integer, ForeignKey('uploads.id'))
    #upload = relationship(Upload,uselist=False,backref='note')


class User(Base):
    __tablename__ = tablebase + 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    accesslevel = Column(Integer,default=99)
    created = Column(DateTime,default=None)
    modified = Column(DateTime,default=None)
    def __repr__(self):
        return self.username

# class Tag(Base):
#   __tablename__ = tablebase + 'tags'
#   id = Column(Integer, primary_key=True)
#   name = Column(String(shortsl))
#   upload








# class AccessMode(Base):
#   __tablename__ = 'accessmode'
#   id = Column(Integer, primary_key=True)
#   info = Column(String(shortsl),default="Access Mode Undefined")

# class Snippet(Base):
#   __tablename__ = 'snippet'
#   id = Column(Integer, primary_key=True)
#   accessmodes = relationship(AccessMode)
#   title = Column(String(200),default="Snippet",nullable=False)
#   accessmode = Column(Integer,ForeignKey('accessmode.id'))
#   body = Column(String)

#   def __repr__(self):
#     return self.body

# class Child(Base):
#   __tablename__ = 'child'
#   id = Column(Integer, primary_key=True)
#   parent = Column(Integer,ForeignKey('snippet.id'),default=None)
#   child = Column(Integer,ForeignKey('snippet.id'),default=None)
#   accessmode = Column(Integer,ForeignKey('snippet.accessmode'),default=0)

# class Notebook(Base):
#   __tablename__ = 'notebook'
#   id = Column(Integer, primary_key=True)
#   title = Column(String(200),default="Notebook Title")

# class AccessItem(Base):
#   __tablename__ = 'accessitem'
#   id = Column(Integer, primary_key=True)
#   snippet = Column(Integer,ForeignKey('snippet.id'),default=None)
#   mode = Column(Integer,ForeignKey('snippet.accessmode'))
#   snippet = relationship(Snippet)
