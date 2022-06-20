import os
import re
import inquirer
import add_module.android_module_files
import add_module.kotlin_module_files

from array import array
from add_module.module_type import ModuleType
from utils.args_utils import get_resolved_location
from utils.jinja_utils import create_environment
from utils.slug_utils import get_slug_for


def invoke(args: dict):
    location = get_resolved_location(args)
    settings_gradle = f'{location}/settings.gradle'

    if not os.path.isfile(settings_gradle):
        raise RuntimeError(
            f'The location {location} is not an Android project')

    module_name = get_slug_for(args['<module>'])

    module_type = select_module_type()
    existing_modules = get_existing_modules(settings_gradle)
    selected_modules = select_modules_dependencies(args, existing_modules)

    create_module(name=module_name, type=module_type, location=location,
                  args=args, dependence_modules=selected_modules)


def create_module(name: str, type: ModuleType, location: str, args: dict, dependence_modules: list):
    env = create_environment('add_module')

    if type == ModuleType.KOTLIN:
        add_module.kotlin_module_files.create(name=name, root=location,
                                              env=env, args=args, dependence_modules=dependence_modules)
    elif type == ModuleType.ANDROID:
        add_module.android_module_files.create(name=name, root=location,
                                               env=env, args=args, dependence_modules=dependence_modules)

    settings_gradle = f'{location}/settings.gradle'
    add_module_to_settings_gradle(settings_gradle, name)


def get_existing_modules(settings_gradle):
    pattern = r"include ':(.+)'"
    f = open(settings_gradle, 'r')
    modules: list = re.findall(pattern, string=f.read(), flags=re.MULTILINE)
    if 'app' in modules:
        modules.remove('app')
    return modules


def select_module_type():
    questions = [inquirer.List(
        name='type-selection',
        message='What kind of module would you add to your project?',
        choices=[ModuleType.KOTLIN.value, ModuleType.ANDROID.value]
    )]
    result = inquirer.prompt(questions)['type-selection']
    return ModuleType(result)


def select_modules_dependencies(args: dict, existing_modules: array):
    if len(existing_modules) == 0:
        return []

    module_name = args['<module>']
    questions = [inquirer.Checkbox(
        'module-selection',
        message=f"Which modules should be a dependency for new module {module_name}?",
        choices=existing_modules,
        carousel=True
    )]
    return inquirer.prompt(questions)['module-selection']


def add_module_to_settings_gradle(settings_gradle: str, module: str):
    lines = []
    with open(settings_gradle, 'r') as f:
        lines = f.readlines()
    with open(settings_gradle, 'w') as f:
        lines.append('\n')
        lines.append(f"include ':{module}'")
        f.writelines(lines)
