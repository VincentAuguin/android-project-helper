import os

from jinja2 import Environment

from utils.args_utils import get_package_name
from utils.error_utils import handle_path_creation
from utils.package_utils import create_package_directories, find_package_name


def create(name: str, root: str, env: Environment, args: dict, dependence_modules: list = []):
    print(f'🛠 {name} module...')
    location = f'{root}/{name}'
    handle_path_creation(location)
    package_name = find_package_name(root)

    create_build_gradle(name, location, env, dependence_modules)
    create_dependencies_gradle(name, location, env)
    create_sources(name, location, env, args, package_name)
    create_proguard_rules(name, location, env)


def create_build_gradle(slug: str, root: str, env: Environment, dependence_modules: list):
    build_gradle = root + '/' + 'build.gradle'
    template = env.get_template('android_module/build.gradle.jinja')

    with open(build_gradle, 'w') as f:
        f.write(template.render(
            module_name=slug,
            dependence_modules=dependence_modules
        ))
    print(f'📄 [:{slug}] build.gradle')


def create_dependencies_gradle(slug: str, root: str, env: Environment):
    gradle_file = root + '/' + 'dependencies.gradle'
    template = env.get_template('android_module/dependencies.gradle.jinja')

    with open(gradle_file, 'w') as f:
        f.write(template.render(module_name=slug))

    print(f'📄 [:{slug}] dependencies.gradle')


def create_proguard_rules(slug: str, root: str, env: Environment):
    proguard_rules = root + '/' + 'proguard-rules.pro'
    template = env.get_template('android_module/proguard-rules.pro.jinja')

    with open(proguard_rules, 'w') as f:
        f.write(template.render())
    print(f'📄 [:{slug}] proguard-rules.pro')


def create_sources(slug: str, root: str, env: Environment, args: dict, package_name: str):
    location = root + '/src'
    os.mkdir(location)

    main_location = location + '/main'
    os.mkdir(main_location)

    create_manifest(slug, main_location, env, package_name)
    create_resources_files(main_location)

    main_location += '/kotlin'
    os.mkdir(main_location)

    create_package_directories(location, package_name)

    test_location = location + '/test'
    os.mkdir(test_location)

    create_unit_test_files(slug, test_location, env, args, package_name)


def create_manifest(slug: str, root: str, env: Environment, package_name: str):
    manifest = root + '/' + 'AndroidManifest.xml'
    template = env.get_template(
        'android_module/src/main/AndroidManifest.xml.jinja')

    with open(manifest, 'w') as f:
        f.write(template.render(package_name=package_name))

    print(f'📄 [:{slug}] AndroidManifest.xml')


def create_resources_files(root: str):
    location = root + '/res'
    os.mkdir(location)


def create_unit_test_files(slug: str, root: str, env: Environment, args: dict, package_name: str):
    location = create_package_directories(root + '/kotlin', package_name)

    example_unit_test_kt = location + '/ExampleUnitTest.kt'
    template = env.get_template(
        'android_module/src/test/kotlin/ExampleUnitTest.kt.jinja')
    with open(example_unit_test_kt, 'w') as f:
        f.write(template.render(package_name=package_name))

    print(f'📄 [:{slug}] Unit test files')
