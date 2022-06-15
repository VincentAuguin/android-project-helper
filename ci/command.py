from utils.args_utils import get_resolved_location
from jinja2 import Environment, PackageLoader

import inquirer


_choices = [
    'Gitlab CI/CD'
]
_questions = [
    inquirer.List(
        name='ci_type',
        message='Which CI solution do you want?',
        choices=_choices,
        carousel=True
    )
]

_gitlab_cicd_choices = [
    'None',
    'Firebase App Distribution'
]
_gitlab_cicd_questions = [
    inquirer.List(
        name='gitlab_cicd_deploy_solution',
        message='Which deployment solution do you want to use?',
        choices=_gitlab_cicd_choices,
        carousel=True
    )
]


def invoke(args: dict):
    env = Environment(loader=PackageLoader("ci"))

    location = get_resolved_location(args)
    type = inquirer.prompt(_questions)['ci_type']

    if type == _choices[0]:
        gitlab_cicd(location, env)
    else:
        raise RuntimeError(f"The specified CI type '{type}' is not recognized")


def gitlab_cicd(location: str, env: Environment):
    yaml = location + '/' + '.gitlab-ci.yml'
    template = env.get_template('.gitlab-ci.yml.jinja')

    input = inquirer.prompt(_gitlab_cicd_questions)
    deploy_solution = input['gitlab_cicd_deploy_solution']
    deploy_with_firebase = deploy_solution == 'Firebase App Distribution'

    with open(yaml, 'w') as f:
        f.write(template.render(
            deploy_with_firebase=deploy_with_firebase
        ))

    print('Next steps:')
    print("""
1. Siging:
    - [Gitlab repository settings > CI/CD > Variables] Add variable as file KEYSTORE_FILE_BASE64
        > Get the base64-encoded content of your keystore:
        base64 -i <your.keystore>
    - [Gitlab repository settings > CI/CD > Variables] Add variable KEYSTORE_ALIAS
    - [Gitlab repository settings > CI/CD > Variables] Add variable KEYSTORE_PASSWORD (masked)""")
    if deploy_with_firebase:
        print("""
2. Firebase App Distribution
    - [.gitlab-ci.yml] Change variable FIREBASE_GROUPS of 'deploy' job, if needed
    - [Gitlab repository settings > CI/CD > Variables] Add variable FIREBASE_TOKEN (masked)
        > Get your CI firebase token by running on your local machine:
        firebase login:ci
    - [Gitlab repository settings > CI/CD > Variables] Add variable FIREBASE_APP_ID
        > Get the app id in Firebase project settings > General > Your apps
        > If you don't have any Firebase app registerd you can add one. You can get the certificate SHA-1/SHA-256 by running:
        keytool -list -v -keystore <your.keystore> -alias <alias>
        Enter keystore password
        Copy the SHA-1 or SHA-256 fingerprint
    - [Gitlab repository settings > CI/CD > Variables] Add variable as file FIREBASE_GOOGLE_SERVICES_JSON_FILE
        > Download the goog-services.json in Firebase project settings > General > Your apps
        > It is necessary to also have it on your local machine under app/ folder, but you should not commit this file""")

    print('\n🦊 .gitlab-ci.yml')
