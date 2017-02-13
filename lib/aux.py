"""
aux.py
Created by Anthony Velardi on 01-16-2017

Global functions! GET YA GLOBAL FUNCTIONS HERE
"""
# -*- coding: utf-8 -*-
import yaml
import ipaddress

def getyaml(fn):
  with open(fn,'r') as f:
    return yaml.load(f.read())

def getconfig():
  return getyaml('config.yaml')

def getsecret():
  return getyaml('secret.yaml')

def validateip(ipaddr,config=getconfig()):
    """
    Tests if a single IP address is valid based on the config
    Note this will eventually also include other prefs that can be overridden
    If valid, return ip object, else return None for validation on other side
    """
    try:
        return ipaddress.ip_address(ipaddr)
    except:
        return None
