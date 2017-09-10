import sys
import os

ROOT_PATH = os.path.realpath(os.path.join(
    os.path.dirname(os.path.realpath(__file__)), os.pardir))
PRJ_PATH = os.path.realpath(os.path.join(
    os.path.dirname(os.path.realpath(__file__))))


CONFIG = dict({
    'log_path': './logs',
    'log_level': 'DEBUG',
    'data': '%s/单轮对话/two_1_2.0_100w.data' % ROOT_PATH,
    'conversations': '%s/conversations' % PRJ_PATH
})

HANLP_CONFIG = dict({
    'url': 'http://localhost:3000'
})

# ElasticSearch Options
# https://elasticsearch-py.readthedocs.io/en/master/api.html#global-options
ELASTICSEARCH_CONFIG = dict({
    'enable': True,
    'url': 'http://localhost:9200/',
    'user': None,
    'pass': None
})
