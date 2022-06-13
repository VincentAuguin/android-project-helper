from nis import match
from utils.args_utils import get_resolved_location
from jinja2 import Environment, PackageLoader

import inquirer


_choices = [
    'Docker (generate a Dockerfile to create an image for your CI agents to run from)'
]
_questions = [
    inquirer.List(
        name='ci_type',
        message='Which CI solution do you want?',
        choices=_choices,
        carousel=True
    )
]


def invoke(args: dict):
    env = Environment(loader=PackageLoader("ci"))

    location = get_resolved_location(args)
    type = inquirer.prompt(_questions)['ci_type']

    if type == _choices[0]:
        docker(location, env)
    else:
        raise RuntimeError(f"The specified CI type '{type}' is not recognized")


def docker(location: str, env: Environment):
    dockerfile = location + '/' + 'Dockerfile'
    template = env.get_template('Dockerfile.jinja')
    with open(dockerfile, 'w') as f:
        f.write(template.render())

    print('🐳 Dockerfile')
