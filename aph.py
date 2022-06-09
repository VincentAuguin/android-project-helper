"""
Android Project Helper

Usage:
  aph create --package-name=<package> [options] <project> [<location>]
  aph help
  aph version

Options:
  --gradle-plugin-version=<version>     Gradle version to use (default is 7.2)
  --min-sdk-version=<version>           Minimum Android SDK API version (default is 24)
  --kotlin-version=<version>            Kotlin version (default is 1.5.21)
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
