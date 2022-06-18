import shutil
import inquirer

from create.git_files import create as create_git_files
from create.gradle_files import create as create_gradle_files
from create.app_module_files import create as create_app_module
from create.domain_module_files import create as create_domain_module
from create.data_module_files import create as create_data_module
import os
from utils import error_utils
from utils.args_utils import get_project_name, get_resolved_project_location
from utils.jinja_utils import create_environment


def invoke(args: dict):
    if args['--verbose']:
        print(args)

    project_name = get_project_name(args)
    location = get_resolved_project_location(args)

    print(f"🔥 Creating Android project '{project_name}' in '{location}'...")
    if os.path.isdir(location):
        override = inquirer.prompt(
            [
                inquirer.Confirm(
                    name='override',
                    message=f"👀 The path {location} already exists. Would you override it?",
                    default=False
                )
            ])['override']

        if not override:
            raise RuntimeError(
                "Creation aborted to not delete conflicting path")
        else:
            print(f"✅ Overriding path '{location}'")
            shutil.rmtree(location)

    os.mkdir(location)

    env = create_environment("create")
    create_git_files(location, env)
    create_gradle_files(location, env, args)
    create_app_module(location, env, args)
    create_domain_module(location, env, args)
    create_data_module(location, env, args)

    warnings = error_utils.create_command_warnings
    print(f"🚀 Android project '{project_name}' created in '{location}'")
    if len(warnings) > 0:
        print(f"🧐 Completed with {len(warnings)} warning(s):")
        for w in warnings:
            print(w)
