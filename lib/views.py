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
    print("Error hit")
    return json.dumps("{message:"+msg+"}"),400


def info():
    return '{"info": "Wallball IP list management tool"}'

def wldump(wlid=None):
    if not wlid:
        s = get_db_session()
        return json.dumps([i.address for i in s.query(IPAddress).order_by(IPAddress.id)])

def addip(ip):
    ip = validateip(ip)
    if not ip:
        error(msg="Invalid IP")
    else:
        #Make sure it's not in the list
        wl = wldump()
        print(wl)
        if ip.exploded in wl:
            return error("IP already in list")
        else:
            i = IPAddress(address=str(ip.exploded))
            s = get_db_session()
            s.add(i)
            s.commit()
            return json.dumps("{'id':'%i'}"%(i.id))

def main():
  pass


if __name__ == "__main__":
  main()
