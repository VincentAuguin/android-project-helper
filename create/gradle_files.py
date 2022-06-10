from utils.error_utils import raise_and_clean
from utils.args_utils import get_compile_sdk_version, get_compose_version, get_kotlin_version, get_gradle_plugin_version, get_min_sdk_version, get_gradle_version, get_target_sdk_version
import os
import shutil

from jinja2 import Environment


def create(root: str, env: Environment, args: dict):
    print('⚙️ Gradle files...')

    create_local_properties(root, env, args)
    create_settings_gradle(root, env, args)
    create_gradle_properties(root, env)
    create_build_gradle(root, env, args)
    create_gradle_wrapper_properties(root, env, args)
    create_gradlew(root)

    print('✅ Gradle files')


def create_local_properties(root: str, env: Environment, args: dict):
    local_properties = root + '/' + 'local.properties'
    template = env.get_template('local.properties.jinja')
    sdk = os.getenv('ANDROID_SDK_ROOT')

    if not sdk:
        message = """
        Please set the environment variable ANDROID_SDK_ROOT:
        export ANDROID_SDK_ROOT=\"path/to/android/sdk\"
        """
        raise_and_clean(message, args)

    with open(local_properties, 'w') as f:
        f.write(template.render(sdk=sdk))

    print('📄 local.properties')


def create_settings_gradle(root: str, env: Environment, args: dict):
    settings_gradle = root + '/' + 'settings.gradle'
    template = env.get_template('settings.gradle.jinja')
    project_name = args['<project>']

    with open(settings_gradle, 'w') as f:
        f.write(template.render(project=project_name))
    print('📄 settings.gradle')


def create_gradle_properties(root: str, env: Environment):
    gradle_properties = root + '/' + 'gradle.properties'
    template = env.get_template('gradle.properties.jinja')

    with open(gradle_properties, 'w') as f:
        f.write(template.render())
    print('📄 gradle.properties')


def create_build_gradle(root: str, env: Environment, args: dict):
    build_gradle = root + '/' + 'build.gradle'
    template = env.get_template('build.gradle.jinja')

    min_sdk_version = get_min_sdk_version(args)
    compile_sdk_version = get_compile_sdk_version(args)
    target_sdk_version = get_target_sdk_version(args)
    kotlin_version = get_kotlin_version(args)
    gradle_plugin_version = get_gradle_plugin_version(args)
    compose_version = get_compose_version(args)

    if min_sdk_version > compile_sdk_version or min_sdk_version > target_sdk_version or target_sdk_version > compile_sdk_version:
        message = f"""
        The provided minimum/target/compile Android SDK versions are not relevant.
        min={min_sdk_version},target={target_sdk_version},compile={compile_sdk_version}
        Please change versions to match this constraint: min <= target <= compile
        """
        raise_and_clean(message, args)

    with open(build_gradle, 'w') as f:
        f.write(template.render(
            min_sdk=min_sdk_version,
            compile_sdk=compile_sdk_version,
            target_sdk=target_sdk_version,
            kotlin_version=kotlin_version,
            gradle_plugin_version=gradle_plugin_version,
            compose_version=compose_version
        ))
    print('📄 build.gradle')


def create_gradle_wrapper_properties(root: str, env: Environment, args: dict):
    location = root + '/' + 'gradle'
    os.mkdir(location)
    location += '/' + 'wrapper'
    os.mkdir(location)
    gradle_wrapper_properties = location + '/' + 'gradle-wrapper.properties'
    template = env.get_template(
        'gradle/wrapper/gradle-wrapper.properties.jinja')

    gradle_version = get_gradle_version(args=args)

    with open(gradle_wrapper_properties, 'w') as f:
        f.write(template.render(gradle_version=gradle_version))

    print('📄 gradle-wrapper.properties')

    shutil.copyfile(os.path.dirname(os.path.realpath(__file__)) +
                    '/executables/gradle-wrapper.jar', location + '/gradle-wrapper.jar')

    print('📄 gradle-wrapper.jar')


def create_gradlew(root: str):
    shutil.copyfile(os.path.dirname(os.path.realpath(__file__)) +
                    '/executables/gradlew', root + '/gradlew')

    print('📄 gradlew')

    shutil.copyfile(os.path.dirname(os.path.realpath(__file__)) +
                    '/executables/gradlew.bat', root + '/gradlew.bat')

    print('📄 gradlew.bat')
