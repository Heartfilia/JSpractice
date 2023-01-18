import sys
# import execjs
from lite_tools import get_time
sys.path.append('../')
from common import match_run

# with open('base.js', 'r', encoding='utf-8') as fp:
#     js = fp.read()
# jsx = execjs.compile(js)

match_run(6)
