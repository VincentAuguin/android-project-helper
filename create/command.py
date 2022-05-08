import shutil

from jinja2 import Environment, PackageLoader

from create.git_files import create as create_git_files
from create.gradle_files import create as create_gradle_files
from create.app_module_files import create as create_app_module
from create.domain_module_files import create as create_domain_module
from create.data_module_files import create as create_data_module
import os


def invoke(args: dict):
    print(args)

    project_name = str(args['<project>'])

    location = args['<location>']
    if not location:
        location = os.getcwd()
    location = os.path.abspath(location)
    location += '/' + project_name.replace(' ', '-')
    print(f"🔥 Creating Android project '{project_name}' in '{location}'...")
    if os.path.isdir(location):
        print(f"⚠️ The path '{location}' already exists, deleting it...")
        shutil.rmtree(location)
        print(f"✅️ Obsolete path '{location}' deleted")

    os.mkdir(location)

    env = Environment(loader=PackageLoader("create"))
    create_git_files(location, env)
    create_gradle_files(location, env, args)
    create_app_module(location, env, args)
    create_domain_module(location, env, args)
    create_data_module(location, env, args)

    print(f"🚀  Android project '{project_name}' created in '{location}'")
