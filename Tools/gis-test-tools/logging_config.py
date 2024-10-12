import logging
from logging.config import dictConfig
from zoautil_py import datasets 

logging_config = dict(
   version = 1,
   formatters = {
      'f': {'format':
            '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}
      },
   handlers = {
      'h': {'class': 'logging.StreamHandler',
            'formatter': 'f',
            'level': logging.DEBUG}
      },
   root = {
      'handlers': ['h'],
      'level': logging.DEBUG,
      },
)

dictConfig(logging_config)