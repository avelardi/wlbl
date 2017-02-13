#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created by Anthony Velardi on 02-13-2017
"""
from aux import getconfig
config = getconfig()
wlblconf = config['defaults']['wlbl']
devmode = wlblconf['devmode']
import json
def getconf():
    return json.dumps(config)
def dbinit():
    if devmode:
        from db import make_tables
        try:
            make_tables()
            return json.dumps({'status':0,'info':'Success! Looks good from here'})
        except:
            return json.dumps({'status':1,'info':'Something broke, check the logs'})
    else:
        return redirect("https://avelardi.github.com", code=302)
