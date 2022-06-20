import add_module.command
from add_module.module_type import ModuleType

from create.git_files import create as create_git_files
from create.gradle_files import create as create_gradle_files
from create.app_module_files import create as create_app_module
from utils import error_utils
from utils.args_utils import get_project_name, get_resolved_project_location
from utils.jinja_utils import create_environment


def invoke(args: dict):
    project_name = get_project_name(args)
    location = get_resolved_project_location(args)

    print(f"🔥 Creating Android project '{project_name}' in '{location}'...")
    error_utils.handle_path_creation(location)

    env = create_environment("create")
    create_git_files(location, env)
    create_gradle_files(location, env, args)
    create_app_module(location, env, args)
    add_module.command.create_module(
        'domain', ModuleType.KOTLIN, location, args, dependence_modules=[])
    add_module.command.create_module(
        'data', ModuleType.ANDROID, location, args, dependence_modules=['domain'])

    warnings = error_utils.create_command_warnings
    print(f"🚀 Android project '{project_name}' created in '{location}'")
    if len(warnings) > 0:
        print(f"🧐 Completed with {len(warnings)} warning(s):")
        for w in warnings:
            print(w)
