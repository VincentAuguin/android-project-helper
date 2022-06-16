import os

from jinja2 import Environment

from utils.args_utils import get_package_name
from utils.package_utils import create_package_directories


def create(root: str, env: Environment, args: dict):
    print('⚙️ Domain module...')
    location = root + '/domain'
    os.mkdir(location)

    create_build_gradle(location, env)
    create_sources(location, env, args)

    print('✅ Domain module')


def create_build_gradle(root: str, env: Environment):
    build_gradle = root + '/' + 'build.gradle'
    template = env.get_template('domain/build.gradle.jinja')

    with open(build_gradle, 'w') as f:
        f.write(template.render())
    print('📄 [:domain] build.gradle')


def create_sources(root: str, env: Environment, args: dict):
    location = root + '/src'
    os.mkdir(location)

    source_files_location = location + '/main/kotlin'
    os.makedirs(source_files_location)

    package_name = get_package_name(args)

    create_package_directories(source_files_location, package_name)

    print('📄 [:domain] Source files')

    test_location = location + '/test/kotlin'
    os.makedirs(test_location)

    create_package_directories(test_location, package_name)

    print('📄 [:domain] Unit test files')
