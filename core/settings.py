"""
Contains settings.

.. data:: CORE_DIR
.. data:: BASE_DIR
.. data:: DEFAULT_DUMP_DIR
.. data:: LOGGING_CONFIG_PATH
.. data:: DEFAULT_CLIENT_HEADERS
.. data:: DEFAULT_MINUTES_TO_SLEEP_ON_NETWORK_ERROR
"""

import pathlib


__all__ = [
    'CORE_DIR',
    'BASE_DIR',
    'DEFAULT_DUMP_DIR',
    'LOGGING_CONFIG_PATH',
    'DEFAULT_CLIENT_HEADERS',
    'DEFAULT_MINUTES_TO_SLEEP_ON_NETWORK_ERROR',
]


CORE_DIR = pathlib.Path(__file__).parent
BASE_DIR = CORE_DIR.parent
DEFAULT_DUMP_DIR = BASE_DIR / 'tmp'
LOGGING_CONFIG_PATH = CORE_DIR / 'utils' / 'logging_' / 'logging_config.yaml'

DEFAULT_CLIENT_HEADERS = {
    'Accept-Language': 'ru'
}

DEFAULT_MINUTES_TO_SLEEP_ON_NETWORK_ERROR = 2
