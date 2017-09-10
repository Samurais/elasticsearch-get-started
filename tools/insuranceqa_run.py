#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) 2017 <> All Rights Reserved
#
#
# File: /Users/hain/ai/elasticsearch-get-started/tools/config.py
# Author: Hai Liang Wang
# Date: 2017-09-10:21:54:17
#
#===============================================================================
'''
ElasticSearch Proxy
https://elasticsearch-py.readthedocs.io/en/master/
'''
from __future__ import print_function
from __future__ import division

__copyright__ = "Copyright (c) 2017 . All Rights Reserved"
__author__    = "Hai Liang Wang"
__date__      = "2017-09-10:21:54:17"


import os
import sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(curdir)

if sys.version_info[0] < 3:
    reload(sys)
    sys.setdefaultencoding("utf-8")
    # raise "Must be using Python 3"

import math
import argparse
from tqdm import tqdm
sys.path.append(os.path.join(os.path.dirname(
    os.path.realpath(__file__)), os.pardir))
from util import log
from services import hanlp_client as hanlp
from services import elasticsearch_client as elasticsearch

# logger
logger = log.getLogger(__file__)

# argv
parser = argparse.ArgumentParser()
parser.add_argument(
    "--pipe-to-es",
    action="store_true", dest="pipe_to_es",
    help="pipe data to elasticsearch service.")

parser.add_argument("--query", action="store_true", dest="query_string",
                    help="Generate Corpus based on previous conversations.")


if __name__ == '__main__':
    # with open('file.txt', 'w') as f:
    #     for x in iter_message_object():
    #         f.write('%s \n' % x.objectId)
    args = parser.parse_args()

    if args.pipe_to_es:
        logger.info('>> create conversations from data')


    if args.query_string:
        logger.info('>> generate corpus')
