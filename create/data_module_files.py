import os

from jinja2 import Environment


def create(root: str, env: Environment, args: dict):
    print('⚙️ Data module...')
    location = root + '/data'
    os.mkdir(location)

    create_build_gradle(location, env)
    create_sources(location, env, args)
    create_proguard_rules(location, env)

    print('✅ Data module')


def create_build_gradle(root: str, env: Environment):
    build_gradle = root + '/' + 'build.gradle'
    template = env.get_template('data/build.gradle.jinja')

    with open(build_gradle, 'w') as f:
        f.write(template.render())
    print('📄 [:data] build.gradle')


def create_proguard_rules(root: str, env: Environment):
    proguard_rules = root + '/' + 'proguard-rules.pro'
    template = env.get_template('data/proguard-rules.pro.jinja')

    with open(proguard_rules, 'w') as f:
        f.write(template.render())
    print('📄 [:data] proguard-rules.pro')


def create_sources(root: str, env: Environment, args: dict):
    package_name = args['--package-name']

    location = root + '/src'
    os.mkdir(location)

    main_location = location + '/main'
    os.mkdir(main_location)

    create_manifest(main_location, env, package_name)
    create_resources_files(main_location)

    main_location += '/kotlin'
    os.mkdir(main_location)

    package_name = args['--package-name']
    packages = package_name.split('.')

    for p in packages:
        main_location += f"/{p}"
        os.mkdir(main_location)

    test_location = location + '/test'
    os.mkdir(test_location)

    create_unit_test_files(test_location, env, package_name)


def create_manifest(root: str, env: Environment, package_name: str):
    manifest = root + '/' + 'AndroidManifest.xml'
    template = env.get_template('data/src/main/AndroidManifest.xml.jinja')

    with open(manifest, 'w') as f:
        f.write(template.render(package_name=package_name))

    print('📄 [:data] AndroidManifest.xml')


def create_resources_files(root: str):
    location = root + '/res'
    os.mkdir(location)


def create_unit_test_files(root: str, env: Environment, package_name: str):
    location = root + '/kotlin'
    os.mkdir(location)

    packages = package_name.split('.')

    for p in packages:
        location += f"/{p}"
        os.mkdir(location)

    example_unit_test_kt = location + '/ExampleUnitTest.kt'
    template = env.get_template(
        'data/src/test/kotlin/ExampleUnitTest.kt.jinja')
    with open(example_unit_test_kt, 'w') as f:
        f.write(template.render(package_name=package_name))

    print('📄 [:data] Unit test files')
