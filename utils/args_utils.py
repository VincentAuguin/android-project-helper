import os

from utils.slug_utils import get_slug_for


def get_package_name(args: dict):
    return args['--package-name']


def get_kotlin_version(args: dict):
    version = args['--kotlin-version']
    if version not in _kotlin_versions_to_compose_versions:
        raise RuntimeError(
            f'The kotlin version provided ({version}) is not supported')
    return version


def get_gradle_plugin_version(args: dict):
    version = args['--gradle-plugin-version']
    if version not in _gradle_plugin_versions_to_gradle_versions:
        raise RuntimeError(
            f'The gradle plugin version provided ({version}) is not supported')
    return version


def get_gradle_version(args: dict):
    plugin_version = get_gradle_plugin_version(args)
    return _gradle_plugin_versions_to_gradle_versions[plugin_version]


def get_min_sdk_version(args: dict):
    version = args['--min-sdk-version']
    return version


def get_compile_sdk_version(args: dict):
    version = args['--compile-sdk-version']
    return version


def get_target_sdk_version(args: dict):
    version = args['--target-sdk-version']
    return version


def get_resolved_location(args: dict):
    location = args['<location>']
    if not location:
        location = os.getcwd()
    location = os.path.abspath(location)
    return location


def get_resolved_project_location(args: dict):
    location = get_resolved_location(args)
    location += '/' + get_slug_for(get_project_name(args))
    return location


def get_project_name(args: dict):
    return str(args['<project>'])


def get_compose_version(args: dict):
    kotlin_version = get_kotlin_version(args)
    return _kotlin_versions_to_compose_versions[kotlin_version]


_gradle_plugin_versions_to_gradle_versions = {
    '7.0.0': '7.0',
    '7.0.1': '7.0',
    '7.0.2': '7.0',
    '7.0.3': '7.0',
    '7.0.4': '7.0',
    '7.1.0': '7.2',
    '7.1.1': '7.2',
    '7.1.2': '7.2',
    '7.1.3': '7.2',
    '7.2.0': '7.3.3',
    '7.2.1': '7.3.3'
}

_kotlin_versions_to_compose_versions = {
    '1.5.10': '1.0.0',
    '1.5.21': '1.0.2',
    '1.5.30': '1.0.3',
    '1.5.31': '1.0.5',
    '1.6.0': '1.1.0-rc01',
    '1.6.10': '1.1.1',
    '1.6.20': '1.2.0-alpha08',
    '1.6.21': '1.2.0-beta03',
}
