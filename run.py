from wlbl import run_api
from lib.aux import getconfig
from lib.db import make_tables

def poop():
  config = getconfig()
  print str(config)
  if config['api']['enabled']:
    run_api(config=config)





if __name__ == '__main__':
  poop()
