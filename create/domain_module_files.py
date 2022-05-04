import os

from jinja2 import Environment


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

    source_files_location = location + '/main'
    os.mkdir(source_files_location)
    source_files_location += '/kotlin'
    os.mkdir(source_files_location)

    package_name = args['--package-name']
    packages = package_name.split('.')

    for p in packages:
        source_files_location += f"/{p}"
        os.mkdir(source_files_location)

    print('📄 [:domain] Source files')

    test_location = location + '/test'
    os.mkdir(test_location)
    test_location += '/kotlin'
    os.mkdir(test_location)

    for p in packages:
        test_location += f"/{p}"
        os.mkdir(test_location)

    print('📄 [:domain] Unit test files')
