import sys
import execjs
from lite_tools import get_time
sys.path.append('../')
from common import match_run


def xxx():
    return 1


match_run(9, xxx, other_headers={"Cookie": "v=Az92JxmHY3wywGSsuyeAK1TJzhjMJJPGrXiXutEM2-414FHG2fQjFr1IJwji"})
