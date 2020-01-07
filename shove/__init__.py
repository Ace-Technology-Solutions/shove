# -*- coding: utf-8 -*-
'''
Common object storage frontend.
'''

from shove.core import Shove
from shove.base import *
from shove.cache import *
import shove.base as shoveBase
import shove.cache as shoveCache
__version__ = (0, 5, 4) # Forked VERSION

__all__ = ['Shove','BaseStore','MemoryStore','DBMStore','ClientStore','SyncStore','FileStore'] + shoveBase.__all__
