"""
Latest Life-Line version of fiji for easy inclusion in Python projects.
"""
__all__ = []
VERSION = '0.0.5'
FIJI_VERSION = '20141125'
URL = 'http://fiji.sc/downloads/Life-Line/fiji-nojre-20141125.zip'

import platform, os

HOME = os.path.expanduser('~')
BIN_FOLDER = os.path.join(HOME, '.bin')
EXTRACT_FOLDER = os.path.join(BIN_FOLDER, 'Fiji.app')
FIJI_ROOT = os.path.join(BIN_FOLDER, 'Fiji-' + FIJI_VERSION + '.app')
BIN_NAMES = {
    'Darwin64bit': os.path.join(FIJI_ROOT, 'Contents/MacOS/ImageJ-macosx'),
    'Linux32bit': os.path.join(FIJI_ROOT, 'ImageJ-linux32'),
    'Linux64bit': os.path.join(FIJI_ROOT, 'ImageJ-linux64'),
    'Windows32bit': os.path.join(FIJI_ROOT, 'ImageJ-win32.exe'),
    'Windows64bit': os.path.join(FIJI_ROOT, 'ImageJ-win64.exe')
}

SYSTEM = platform.system() + platform.architecture()[0]
BIN = BIN_NAMES[SYSTEM]
