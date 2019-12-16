#!C:\Python27\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'conan==1.12.3','console_scripts','conan_server'
__requires__ = 'conan==1.12.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('conan==1.12.3', 'console_scripts', 'conan_server')()
    )
