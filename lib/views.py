#!/usr/bin/env python
"""
Created by Anthony Velardi on 02-12-2017
"""
from connexion import NoContent
from aux import getconfig, validateip
from lib.models import IPAddress
import ipaddress
import json
from flask import redirect
from lib.db import get_db_session

config = getconfig()
wlblconf = config['defaults']['wlbl']
devmode = wlblconf['devmode']


def error(msg="No information available"):
  return str(msg),400


def info():
    return '{"info": "Wallball IP list management tool"}'

def wldump(wlid=None):
    if not wlid:
        s = get_db_session()
        return json.dumps([i.address for i in s.query(IPAddress).order_by(IPAddress.id)])

def addip(ipaddr):
    ip = validateip(ipaddr)
    s = get_db_session()
    s.add(note)
    s.commit()

def main():
  pass


if __name__ == "__main__":
  main()
