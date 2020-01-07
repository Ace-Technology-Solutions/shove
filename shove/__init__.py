# -*- coding: utf-8 -*-
'''
Common object storage frontend.
'''
print("Correct init run")
from shove.core import Shove
from shove.base import *
from shove.cache import *
import shove.base as shoveBase
import shove.cache as shoveCache
import shove.store as shoveStore
__version__ = (0, 5, 4) # Forked VERSION

__all__ = ['Shove','BaseStore','MemoryStore','DBMStore','ClientStore','SyncStore','FileStore'] + shoveBase.__all__ + shoveStore.__all__
