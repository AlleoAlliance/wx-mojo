import platform

if platform.system() != 'Windows':
    raise Exception("当前操作系统不是 Windows")

from core import *
from .OcrManager import *
from utils.detect import *
from utils.winapi import *
