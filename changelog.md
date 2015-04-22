# 0.3.0
- fix python2.7 os.fdopen error
- add test
- add travis testing

# 0.2.1
- include VERSION in source package

# 0.2.0
- download fiji on import instead of in setup.py (which never runs for
  wheel installs)

# 0.1.0
- use pydebug for debugging messages
- added API reference docs
- fix JRE on windows
- fix temp file permission trouble on windows

# 0.0.5
- macro.run: return existing output_files even if macro empty

# 0.0.4
- macro.stitch: support for 16 bit images

# 0.0.3
- add fijibin.macro

# 0.0.2
- use 64-bit Fiji if operating system is 64-bit

# 0.0.1
- use `BIN` as variable name
- chmod +x for bin_names after fetch
- VERSION -> FIJI_VERSION
- use Fiji version name
  - Fiji.app -> Fiji-20141125.app

# 2014.11.25 (removed from pypi)
- initial version
