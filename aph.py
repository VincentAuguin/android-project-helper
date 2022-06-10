"""
Android Project Helper

Usage:
  aph create --package-name=<package> [options] <project> [<location>]
  aph help
  aph version

Options:
  --min-sdk-version=<version>           Minimum Android SDK API version (default is 26)
  --compile-sdk-version=<version>       Compile Android SDK API version (default is 33)
  --target-sdk-version=<version>        Target Android SDK API version (default is 31)
  --gradle-plugin-version=<version>     Gradle version to use (default is 7.2.1)
                                        [7.0.0-4, 7.1.0-3, 7.2.0-1]
  --kotlin-version=<version>            Kotlin version (default is 1.6.10)
                                        [1.5.10, 1.5.21, 1.5.30, 1.5.31, 1.6.0, 1.6.10, 1.6.20, 1.6.21]
  -f, --force                           Override existing destination if the generated directory already exists
  -v, --verbose                         Print more verbose logs
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
