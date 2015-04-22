# fijibin
This software will download the latest *Life-Line* version of
[Fiji](http://fiji.sc/), make the correct cross-platform binary available and
provide a macro submodule which makes automation of Fiji trivial from python.

**Video demo**

[![](http://img.youtube.com/vi/v0q88SisBtw/0.jpg)](http://youtu.be/v0q88SisBtw)

Current Fiji Life-Line version in this package is **2014 November 25**.

If you experience any trouble with this module, please
[submit an issue](https://github.com/arve0/fijibin/issues/new) or send a
pull request on github.

## Install
```
pip install fijibin
```

## Usage
```python
>>> import fijibin
>>> fijibin.BIN
'/Users/arve/.bin/Fiji.app/Contents/MacOS/ImageJ-macosx'
>>> fijibin.FIJI_VERSION
'20141125'
```

`fijibin.BIN` will point to linux, mac or windows version, depending on the
operating system detected via [platform](https://docs.python.org/3.4/library/platform.html).

### Macros
```python
import fijibin.macro
macro.run(macro_string_or_list_of_strings)
```

### Refetch binary
```python
>>> from fijibin.fetch import fetch
>>> fetch()
```

See more in the [API reference](http://fijibin.readthedocs.org/).

## Development
Install dependencies and link development version of fijibin to pip:
```bash
git clone https://github.com/arve0/fijibin
cd fijibin
pip install -r requirements.txt
```

### run test
```bash
pip install tox
tox
```

### extra output, jump into pdb upon error
```bash
DEBUG=fijibin tox -- --pdb -s
```

### build api reference
```bash
pip install -r docs/requirements.txt
make docs
```
