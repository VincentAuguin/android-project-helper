def get_kotlin_version(args: dict):
    version = args['--kotlin-version']
    if not version:
        version = '1.5.21'
    return version


def get_gradle_plugin_version(args: dict):
    version = args['--gradle-plugin-version']
    if not version:
        version = '7.2'
    return version


def get_gradle_version(args: dict):
    plugin_version = get_gradle_plugin_version(args)
    return _gradle_versions[plugin_version]


def get_min_sdk_version(args: dict):
    version = args['--min-sdk-version']
    if not version:
        version = '24'
    return version


_gradle_versions = {
    '7.0': '7.0',
    '7.1': '7.2',
    '7.2': '7.3.3'
}
