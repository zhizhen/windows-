#!C:\Python27\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'keyring==8.7','console_scripts','keyring'
__requires__ = 'keyring==8.7'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('keyring==8.7', 'console_scripts', 'keyring')()
    )
