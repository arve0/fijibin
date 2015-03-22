"""
Latest Life-Line version of fiji for easy inclusion in Python projects.
"""
import sys, os, platform, stat, shutil
from io import BytesIO
from zipfile import ZipFile
from os.path import join, dirname
from . import macro
try:
    from zipfile import BadZipZile
except ImportError:
    from zipfile import BadZipfile
    BadZipFile = BadZipfile

__all__ = ['fetch', 'macro']


##
# CONSTANTS
##

VERSION = open(join(dirname(__file__), 'VERSION')).read().strip()
FIJI_VERSION = '20141125'
BASE_URL = 'http://fiji.sc/downloads/Life-Line/fiji-'
END_URL = '-' + FIJI_VERSION + '.zip'

HOME = os.path.expanduser('~')
BIN_FOLDER = join(HOME, '.bin')
EXTRACT_FOLDER = join(BIN_FOLDER, 'Fiji.app')
FIJI_ROOT = join(BIN_FOLDER, 'Fiji-' + FIJI_VERSION + '.app')
BIN_NAMES = {
    'Darwin64bit': join(FIJI_ROOT, 'Contents/MacOS/ImageJ-macosx'),
    'Linux32bit': join(FIJI_ROOT, 'ImageJ-linux32'),
    'Linux64bit': join(FIJI_ROOT, 'ImageJ-linux64'),
    'Windows32bit': join(FIJI_ROOT, 'ImageJ-win32.exe'),
    'Windows64bit': join(FIJI_ROOT, 'ImageJ-win64.exe')
}

_unix_url = BASE_URL + 'nojre' + END_URL
URLS = {
    'Darwin64bit': _unix_url,
    'Linux32bit': _unix_url,
    'Linux64bit': _unix_url,
    'Windows32bit': BASE_URL + 'win32' + END_URL,
    'Windows64bit': BASE_URL + 'win64'  + END_URL
}

SYSTEM = platform.system() + platform.architecture()[0]
BIN = BIN_NAMES[SYSTEM]
URL = URLS[SYSTEM]


##
# FETCH BINARY
##
def fetch(force=False):
    """Fetch and extract latest Life-Line version of Fiji is just ImageJ
    to *~/.bin*.

    Parameters
    ----------
    force : bool
        Force overwrite of existing Fiji in *~/.bin*.

    """
    try:
        # python 2
        from urllib2 import urlopen, HTTPError, URLError
    except ImportError:
        # python 3
        from urllib.request import urlopen, HTTPError, URLError

    if os.path.isdir(FIJI_ROOT) and not force:
        return
    elif not os.path.isdir(FIJI_ROOT):
        print('Fiji missing in %s' % FIJI_ROOT)

    if force:
        print('Deleting %s' % FIJI_ROOT)
        shutil.rmtree(FIJI_ROOT, ignore_errors=True)

    print('Downloading fiji from %s' % URL)
    try:
        req = urlopen(URL)
        try:
            size = int(req.info()['content-length'])
        except AttributeError:
            size = -1

        chunk = 512*1024
        fp = BytesIO()
        i = 0
        while 1:
            data = req.read(chunk)
            if not data:
                break
            fp.write(data)
            if size > 0:
                percent = fp.tell() // (size/100)
                msg = 'Downloaded %d percent      \r' % percent
            else:
                msg = 'Downloaded %d bytes\r' % fp.tell()
            sys.stdout.write(msg)
    except (HTTPError, URLError) as e:
        print('Error getting fiji: {}'.format(e))
        sys.exit(1)

    try:
        print('\nExtracting zip')
        z = ZipFile(fp)
        z.extractall(BIN_FOLDER)
        # move to Fiji-VERSION.app to easily check if it exists (upon fijibin upgrade)
        os.rename(EXTRACT_FOLDER, FIJI_ROOT)
    except (BadZipFile, IOError) as e:
        print('Error extracting zip: {}'.format(e))
        sys.exit(1)

    for path in BIN_NAMES.values():
        st = os.stat(path)
        os.chmod(path, st.st_mode | stat.S_IEXEC)

##
# Download upon import if Fiji is missing
##
fetch()
