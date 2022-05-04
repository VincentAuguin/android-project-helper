"""
Android Project Helper

Usage:
  aph.py create --package-name=<package> [--gradle-version=<version> --min-sdk-version=<minSdkVersion>] <project> [<location>]
  aph.py help
  aph.py version
"""

from docopt import docopt

from version.command import invoke as version_command
from create.command import invoke as create_command


def main():
    args = docopt(__doc__)

    if args['version']:
        version_command()
    elif args['create']:
        create_command(args)
    else:
        print(__doc__)


if __name__ == '__main__':
    main()
