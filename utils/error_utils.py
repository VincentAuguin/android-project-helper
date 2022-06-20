import shutil
import os
import inquirer

from utils import args_utils


def raise_and_clean(msg: str, args: dict):
    location = args_utils.get_resolved_project_location(args)
    shutil.rmtree(location)
    raise RuntimeError(msg)


def handle_path_creation(path: str):
    if os.path.isdir(path):
        override = inquirer.prompt(
            [
                inquirer.Confirm(
                    name='override',
                    message=f"👀 The path {path} already exists. Would you override it?",
                    default=False
                )
            ])['override']

        if not override:
            raise RuntimeError(
                "Creation aborted to not delete conflicting path")
        else:
            print(f"✅ Overriding path '{path}'")
            shutil.rmtree(path)

    os.mkdir(path)


create_command_warnings = []
