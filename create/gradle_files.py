import os
import shutil

from jinja2 import Environment


def create(root: str, env: Environment, args: dict):
    print('⚙️ Gradle files...')

    create_local_properties(root, env)
    create_settings_gradle(root, env, args)
    create_gradle_properties(root, env)
    create_build_gradle(root, env, args)
    create_gradle_wrapper_properties(root, env, args)
    create_gradlew(root)

    print('✅ Gradle files')


def create_local_properties(root: str, env: Environment):
    local_properties = root + '/' + 'local.properties'
    template = env.get_template('local.properties.jinja')
    sdk = os.getenv('ANDROID_SDK_ROOT')

    if not sdk:
        print('Please set the environment variable ANDROID_SDK_ROOT')
        return

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
    min_sdk_version = args['--min-sdk-version']

    if not min_sdk_version:
        min_sdk_version = "24"

    with open(build_gradle, 'w') as f:
        f.write(template.render(min_sdk=min_sdk_version))
    print('📄 build.gradle')


def create_gradle_wrapper_properties(root: str, env: Environment, args: dict):
    location = root + '/' + 'gradle'
    os.mkdir(location)
    location += '/' + 'wrapper'
    os.mkdir(location)
    gradle_wrapper_properties = location + '/' + 'gradle-wrapper.properties'
    template = env.get_template('gradle/wrapper/gradle-wrapper.properties.jinja')

    gradle_version = args['--gradle-version']
    if not gradle_version:
        gradle_version = "7.2"

    with open(gradle_wrapper_properties, 'w') as f:
        f.write(template.render(gradle_version=gradle_version))

    print('📄 gradle-wrapper.properties')

    shutil.copyfile(os.path.dirname(os.path.realpath(__file__)) + '/executables/gradle-wrapper.jar', location + '/gradle-wrapper.jar')

    print('📄 gradle-wrapper.jar')


def create_gradlew(root: str):
    shutil.copyfile(os.path.dirname(os.path.realpath(__file__)) + '/executables/gradlew', root + '/gradlew')

    print('📄 gradlew')

    shutil.copyfile(os.path.dirname(os.path.realpath(__file__)) + '/executables/gradlew.bat', root + '/gradlew.bat')

    print('📄 gradlew.bat')
