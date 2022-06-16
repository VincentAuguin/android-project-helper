import os
import shutil

from jinja2 import Environment
from shutil import ignore_patterns
from utils.args_utils import get_package_name

from utils.package_utils import create_package_directories


def create(root: str, env: Environment, args: dict):
    print('⚙️ App module...')
    location = root + '/app'
    os.mkdir(location)

    create_build_gradle(location, env, args)
    create_proguard_rules(location, env)
    create_sources(location, env, args)

    print('✅ App module')


def create_build_gradle(root: str, env: Environment, args: dict):
    build_gradle = root + '/' + 'build.gradle'
    template = env.get_template('app/build.gradle.jinja')
    package_name = args['--package-name']

    with open(build_gradle, 'w') as f:
        f.write(template.render(package_name=package_name))
    print('📄 [:app] build.gradle')


def create_proguard_rules(root: str, env: Environment):
    proguard_rules = root + '/' + 'proguard-rules.pro'
    template = env.get_template('app/proguard-rules.pro.jinja')

    with open(proguard_rules, 'w') as f:
        f.write(template.render())
    print('📄 [:app] proguard-rules.pro')


def create_sources(root: str, env: Environment, args: dict):
    location = root + '/src'
    os.mkdir(location)

    main_location = location + '/main'
    os.mkdir(main_location)

    create_manifest(main_location, env, args)
    create_main_files(main_location, env, args)
    create_resources_files(main_location, env, args)

    test_location = location + '/test'
    os.mkdir(test_location)

    create_unit_test_files(test_location, env, args)

    instrumented_test_location = location + '/androidTest'
    os.mkdir(instrumented_test_location)

    create_instrumented_test_files(
        instrumented_test_location, env, args)


def create_manifest(root: str, env: Environment, args: dict):
    manifest = root + '/' + 'AndroidManifest.xml'
    template = env.get_template('app/src/main/AndroidManifest.xml.jinja')

    package_name = get_package_name(args)

    app_class_name = str(args['<project>']).title(
    ).strip().replace(' ', '') + 'App'
    theme_name = 'Theme.' + \
        str(args['<project>']).title().strip().replace(' ', '')

    with open(manifest, 'w') as f:
        f.write(template.render(
            package_name=package_name,
            app_class_name=app_class_name,
            theme_name=theme_name
        ))

    print('📄 [:app] AndroidManifest.xml')


def create_main_files(root: str, env: Environment, args: dict):
    package_name = get_package_name(args)
    location = create_package_directories(root + '/kotlin', package_name)

    app_class_name = str(args['<project>']).title(
    ).strip().replace(' ', '') + 'App'
    application = location + '/' + app_class_name + '.kt'
    template = env.get_template('app/src/main/kotlin/App.kt.jinja')

    with open(application, 'w') as f:
        f.write(template.render(
            package_name=package_name,
            app_class_name=app_class_name
        ))

    main_activity = location + '/MainActivity.kt'
    template = env.get_template('app/src/main/kotlin/MainActivity.kt.jinja')

    theme_name = str(args['<project>']).title(
    ).strip().replace(' ', '') + 'Theme'

    with open(main_activity, 'w') as f:
        f.write(template.render(
            package_name=package_name,
            theme_name=theme_name
        ))

    create_theme_files(location, env, args, theme_name)

    print('📄 [:app] Source files')


def create_resources_files(root: str, env: Environment, args: dict):
    location = root + '/res'

    src = os.path.dirname(__file__)
    shutil.copytree(src=src + '/templates/app/src/main/res',
                    dst=location, ignore=ignore_patterns('values'))

    values_location = location + '/values'
    os.mkdir(values_location)

    strings_xml = values_location + '/strings.xml'
    template = env.get_template('/app/src/main/res/values/strings.xml.jinja')

    with open(strings_xml, 'w') as f:
        f.write(template.render(
            app_name=args['<project>']
        ))

    themes_xml = values_location + '/themes.xml'
    template = env.get_template('/app/src/main/res/values/themes.xml.jinja')
    theme_name = 'Theme.' + \
        str(args['<project>']).title().strip().replace(' ', '')

    with open(themes_xml, 'w') as f:
        f.write(template.render(
            theme_name=theme_name
        ))

    print('📄 [:app] XML Resource files')


def create_theme_files(root: str, env: Environment, args: dict, theme_name: str):
    location = root + '/shared/theme'
    os.makedirs(location)

    color_kt = location + '/Color.kt'
    shape_kt = location + '/Shape.kt'
    theme_kt = location + '/Theme.kt'
    type_kt = location + '/Type.kt'

    package_name = get_package_name(args)

    template = env.get_template(
        'app/src/main/kotlin/shared/theme/Color.kt.jinja')
    with open(color_kt, 'w') as f:
        f.write(template.render(package_name=package_name))

    template = env.get_template(
        'app/src/main/kotlin/shared/theme/Shape.kt.jinja')
    with open(shape_kt, 'w') as f:
        f.write(template.render(package_name=package_name))

    template = env.get_template(
        'app/src/main/kotlin/shared/theme/Theme.kt.jinja')
    with open(theme_kt, 'w') as f:
        f.write(template.render(
            package_name=package_name,
            theme_name=theme_name
        ))

    template = env.get_template(
        'app/src/main/kotlin/shared/theme/Type.kt.jinja')
    with open(type_kt, 'w') as f:
        f.write(template.render(package_name=package_name))


def create_unit_test_files(root: str, env: Environment, args: dict):
    package_name = get_package_name(args)
    location = create_package_directories(root + '/kotlin', package_name)

    example_unit_test_kt = location + '/ExampleUnitTest.kt'
    template = env.get_template('app/src/test/kotlin/ExampleUnitTest.kt.jinja')
    with open(example_unit_test_kt, 'w') as f:
        f.write(template.render(package_name=package_name))

    print('📄 [:app] Unit test files')


def create_instrumented_test_files(root: str, env: Environment, args: dict):
    package_name = get_package_name(args)
    location = create_package_directories(root + '/kotlin', package_name)

    example_instrumented_test_kt = location + '/ExampleInstrumentedTest.kt'
    template = env.get_template(
        'app/src/androidTest/kotlin/ExampleInstrumentedTest.kt.jinja')
    with open(example_instrumented_test_kt, 'w') as f:
        f.write(template.render(package_name=package_name))

    print('📄 [:app] Instrumented test files')
