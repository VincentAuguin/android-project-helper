import shutil

from jinja2 import Environment, PackageLoader

from create.git_files import create as create_git_files
from create.gradle_files import create as create_gradle_files
from create.app_module_files import create as create_app_module
from create.domain_module_files import create as create_domain_module
from create.data_module_files import create as create_data_module
import os
from utils.args_utils import get_project_name, get_resolved_project_location


def invoke(args: dict):
    if args['--verbose']:
        print(args)

    project_name = get_project_name(args)
    location = get_resolved_project_location(args)

    print(f"🔥 Creating Android project '{project_name}' in '{location}'...")
    if os.path.isdir(location):
        override = args['--force']
        if not override:
            raise RuntimeError(f"The path '{location}' already exists")
        else:
            print(f"👀 Overriding path '{location}'")
            shutil.rmtree(location)

    os.mkdir(location)

    env = Environment(loader=PackageLoader("create"))
    create_git_files(location, env)
    create_gradle_files(location, env, args)
    create_app_module(location, env, args)
    create_domain_module(location, env, args)
    create_data_module(location, env, args)

    print(f"🚀  Android project '{project_name}' created in '{location}'")
