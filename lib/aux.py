"""
aux.py
Created by Anthony Velardi on 01-16-2017

Global functions! GET YA GLOBAL FUNCTIONS HERE
"""
import yaml

def getyaml(fn):
  with open(fn,'r') as f:
    return yaml.load(f.read())

def getconfig():
  return getyaml('config.yaml')

def getsecret():
  return getyaml('secret.yaml')
