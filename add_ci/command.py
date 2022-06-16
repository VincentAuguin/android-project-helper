from utils.args_utils import get_resolved_location
from utils.slug_utils import get_slug_for
from add_ci.gitlab_ci_cd import add_gitlab_ci_cd
from add_ci.jenkins import add_jenkins
from add_ci.bitrise import add_bitrise
from jinja2 import Environment, PackageLoader

import inquirer
import os


_ci_type_choices = [
    'Bitrise',
    'Gitlab CI/CD',
    'Jenkins'
]
_ci_deploy_solution_choices = [
    'None',
    'Firebase App Distribution'
]
_questions = [
    inquirer.List(
        name='ci_type',
        message='Which CI solution do you want?',
        choices=_ci_type_choices,
        carousel=True
    ),
    inquirer.List(
        name='deploy_solution',
        message='Which deployment solution do you want to use?',
        choices=_ci_deploy_solution_choices,
        carousel=True
    )
]


def invoke(args: dict):
    env = Environment(loader=PackageLoader(__package__))

    location = get_resolved_location(args)
    if not os.path.isdir(location):
        os.makedirs(location)

    answers = inquirer.prompt(_questions)

    type_slug = get_slug_for(answers['ci_type'])

    deploy_solution_slug = get_slug_for(str(answers['deploy_solution']))

    if type_slug == 'bitrise':
        add_bitrise(location, env, deploy_solution_slug)
    elif type_slug == 'gitlab-ci-cd':
        add_gitlab_ci_cd(location, env, deploy_solution_slug)
    elif type_slug == 'jenkins':
        add_jenkins(location, env, deploy_solution_slug)
    else:
        raise RuntimeError(f"The specified CI type '{type}' is not recognized")
