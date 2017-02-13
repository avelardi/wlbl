from wlbl import run_api
from lib.aux import getconfig
from lib.db import make_tables



##Todo build preflight check
def poop():
  config = getconfig()
  if config['api']['enabled']:
    run_api(config=config)




if __name__ == '__main__':
  poop()
