import os

from jinja2 import Environment


def create(root: str, env: Environment, args: dict):
    print('⚙️ Data module...')
    location = root + '/data'
    os.mkdir(location)

    create_build_gradle(location, env)
    create_sources(location, env, args)

    print('✅ Data module')


def create_build_gradle(root: str, env: Environment):
    build_gradle = root + '/' + 'build.gradle'
    template = env.get_template('data/build.gradle.jinja')

    with open(build_gradle, 'w') as f:
        f.write(template.render())
    print('📄 [:data] build.gradle')