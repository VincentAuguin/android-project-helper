import shutil

from jinja2 import Environment, PackageLoader

from create.git_files import create as create_git_files
from create.gradle_files import create as create_gradle_files
from create.app_module_files import create as create_app_module
import os


def invoke(args: dict):
    print(args)

    project_name = str(args['<project>'])
    cwd = os.getcwd()
    root = cwd + '/' + project_name.replace(' ', '-')
    print(f"🔥 Creating Android project '{project_name}' in '{root}'...")
    if os.path.isdir(root):
        print(f"⚠️ The path '{root}' already exists, deleting it...")
        shutil.rmtree(root)
        print(f"✅️ Obsolete path '{root}' deleted")

    os.mkdir(root)

    env = Environment(loader=PackageLoader("create"))
    create_git_files(root, env)
    create_gradle_files(root, env, args)
    create_app_module(root, env, args)

    print(f"🚀  Android project '{project_name}' created in '{root}'")
