# fijibin
This software will download the latest *Life-Line* version of [Fiji](http://fiji.sc/)
and make the binary easily available from python.

## Install
```
pip install fijibin
```

## Use
```python
>>> import fijibin
>>> fijibin.bin
'/Users/arve/.bin/Fiji.app/Contents/MacOS/ImageJ-macosx'
```

`fijibin.bin` will point to linux, mac or windows version, depending on the
operating system detected via [platform](https://docs.python.org/3.4/library/platform.html).
