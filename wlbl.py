import connexion
import logging
from api.lib.aux import getconfig
"""
api.py
Created by Anthony Velardi on 01-15-2017

Base api server functions with config loaded from ./config.yaml
"""
def server(config):
  logging.basicConfig(level=logging.INFO)
  apiapp = connexion.App(__name__, specification_dir=config['api']['specdir'])
  for spec in config['api']['specs']:
    spec_config = config['api']['specs'][spec]
    file_path = spec_config['filename']
    apiapp.add_api(file_path,strict_validation=spec_config['strictvalidation'],base_path=spec_config['basepath'])
  return apiapp

def run_api(config=getconfig()):
  srvr = server(config)
  srvr.run(host=config['api']['flask']['host'],port=config['api']['flask']['port'],debug=config['api']['flask']['debug'])
