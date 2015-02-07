"""
Latest Life-Line version of fiji for easy inclusion in Python projects.
"""
__all__ = []
VERSION = '14.11.25'

import platform, os

system = platform.system()
if system == 'Linux':
    bin = 'Fiji.app/ImageJ-linux32'
elif system == 'Windows':
    bin = 'Fiji.app/ImageJ-linux32'
elif system == 'Darwin':
    bin = 'Fiji.app/Contents/MacOS/ImageJ-macosx'

bin_folder = os.path.expanduser('~')
bin_folder = os.path.join(bin_folder, '.bin')
bin = os.path.join(bin_folder, bin)
