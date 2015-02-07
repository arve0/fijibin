#!/usr/bin/env python
import sys, os
from io import BytesIO
from zipfile import ZipFile
try:
    from zipfile import BadZipZile
except ImportError:
    from zipfile import BadZipfile
    BadZipFile = BadZipfile

home = os.path.expanduser('~')
folder = os.path.join(home, '.bin')

def fetch():
    "Fetch and extract latest Life-Line version of Fiji is just ImageJ to `~/.bin`."
    if os.path.isdir(os.path.join(folder,'Fiji.app')):
        print('Fiji.app already exists in ~/.bin, not downloading.')
        return

    try:
        # python 2
        from urllib2 import urlopen, HTTPError, URLError
    except ImportError:
        # python 3
        from urllib.request import urlopen, HTTPError, URLError


    url = 'http://fiji.sc/downloads/Life-Line/fiji-nojre-20141125.zip'

    try:
        print('Getting fiji from %s' % url)
        req = urlopen(url)
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
        z.extractall(folder)
    except (BadZipFile, IOError) as e:
        print('Error extracting zip: {}'.format(e))
        sys.exit(1)
