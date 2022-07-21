import os

from jinja2 import Environment

from utils.error_utils import handle_path_creation
from utils.package_utils import create_package_directories, find_package_name


def create(name: str, root: str, env: Environment, args: dict, dependence_modules: list = []):
    print(f'🛠 {name} module...')
    location = f'{root}/{name}'
    handle_path_creation(location)
    package_name = find_package_name(root)

    create_build_gradle(name, location, env, dependence_modules)
    create_dependencies_gradle(name, location, env)
    create_sources(name, location, args, package_name)


def create_build_gradle(slug: str, root: str, env: Environment, dependence_modules: list):
    build_gradle = root + '/' + 'build.gradle'
    template = env.get_template('kotlin_module/build.gradle.jinja')

    with open(build_gradle, 'w') as f:
        f.write(template.render(
            module_name=slug,
            dependence_modules=dependence_modules
        ))
    print(f'📄 [:{slug}] build.gradle')


def create_dependencies_gradle(slug: str, root: str, env: Environment):
    gradle_file = root + '/' + 'dependencies.gradle'
    template = env.get_template('kotlin_module/dependencies.gradle.jinja')

    with open(gradle_file, 'w') as f:
        f.write(template.render(module_name=slug))

    print(f'📄 [:{slug}] dependencies.gradle')


def create_sources(slug: str, root: str, args: dict, package_name: str):
    location = root + '/src'
    os.mkdir(location)

    source_files_location = location + '/main/kotlin'
    os.makedirs(source_files_location)

    create_package_directories(source_files_location, package_name)

    print(f'📄 [:{slug}] Source files')

    test_location = location + '/test/kotlin'
    os.makedirs(test_location)

    create_package_directories(test_location, package_name)

    print(f'📄 [:{slug}] Unit test files')
