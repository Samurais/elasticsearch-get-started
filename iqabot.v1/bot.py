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
from config import CORPUS_CONFIG

# logger
logger = log.getLogger(__file__)

# argv
parser = argparse.ArgumentParser()
parser.add_argument(
    "--pipe-to-es",
    action="store_true", dest="pipe_to_es",
    help="Pipe data to ElasticSearch Service.")

parser.add_argument("--query", 
                    help="Query question to get answers from ElasticSearch Service.")

INDEX_INSU = "insuranceqa"
stopwords = []


def query_es(query):
    '''
    Query
    '''
    global stopwords
    if len(stopwords) == 0:
        with open(os.path.join(curdir, 'stopwords.txt'), "r") as fin:
            [stopwords.append(x.strip()) for x in fin]
    _query = []
    for x in hanlp.cut(query, type="index")['data']:
        if not x['word'] in stopwords:
            # print(x['word'], x['nature'])
            _query.append(x['word'])
    if len(_query) > 0:
        print("query: %s" % " ".join(_query))
        resp = elasticsearch.search(index=INDEX_INSU, terms=_query)
        if len(resp["hits"]["hits"]) > 0:
            for o in resp["hits"]["hits"]:
                print("hit %s : %s score: %s" % (o["_source"]["id"], o["_source"]["post"], o["_score"]))
        print("total: %d" % resp["hits"]["total"])
    return resp

def import_es_data():
    with open(CORPUS_CONFIG["valid"], "r") as fin:
        for l in fin:
            r = l.split(" ++$++ ")
            id = r[0]
            category = r[1]
            post = r[2]
            terms = r[3]
            print(">> pipe ", category, post, terms)
            elasticsearch.index(id, dict({
                "id": id,
                "category": category,
                "post": post,
                "terms": terms 
            }), index = INDEX_INSU, doc_type="zh_CN")

if __name__ == '__main__':
    args = parser.parse_args()

    if args.pipe_to_es:
        logger.info('>> pipe data to ElasticSearch Service ...')
        import_es_data()

    if args.query:
        logger.info('>> query question to get answers from ElasticSearch Service query: \n %s' % args.query)
        query_es(args.query)