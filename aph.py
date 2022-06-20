"""
Android Project Helper
https://github.com/VincentAuguin/android-project-helper

Usage:
  aph create --package-name=package [options] <project> [<location>]
  aph add:module <module> [<location>]
  aph add:ci [<location>]
  aph help

Create options:
  --min-sdk-version=version               Minimum Android SDK API version [default: 26]
  --compile-sdk-version=version           Compile Android SDK API version [default: 33]
  --target-sdk-version=version            Target Android SDK API version [default: 31]
  --gradle-plugin-version=version         Gradle version to use [default: 7.2.1]
                                          [7.0.0-4, 7.1.0-3, 7.2.0-1]
  --kotlin-version=version                Kotlin version [default: 1.6.10]
                                          [1.5.10, 1.5.21, 1.5.30, 1.5.31, 1.6.0, 1.6.10, 1.6.20, 1.6.21]

General options
  -v, --verbose                           Print more verbose logs
"""

from docopt import docopt

from create.command import invoke as create_command
from add_module.command import invoke as module_command
from add_ci.command import invoke as ci_command


def main():
    args = docopt(__doc__)

    if args['--verbose']:
        print(args)

    if args['create']:
        create_command(args)
    elif args['add:module']:
        module_command(args)
    elif args['add:ci']:
        ci_command(args)
    else:
        print(__doc__)


if __name__ == '__main__':
    try:
        main()
    except RuntimeError as err:
        print(f'\n❌ Failed: {str(err)}')
