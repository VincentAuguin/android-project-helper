from utils.args_utils import get_resolved_location
from jinja2 import Environment, PackageLoader

import inquirer

from utils.slug_utils import get_slug_for


_ci_type_choices = [
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
    env = Environment(loader=PackageLoader("ci"))

    location = get_resolved_location(args)

    answers = inquirer.prompt(_questions)

    type_slug = get_slug_for(answers['ci_type'])

    deploy_solution_slug = get_slug_for(str(answers['deploy_solution']))

    if type_slug == 'gitlab-ci-cd':
        gitlab_cicd(location, env, deploy_solution_slug)
    elif type_slug == 'jenkins':
        jenkins(location, env, deploy_solution_slug)
    else:
        raise RuntimeError(f"The specified CI type '{type}' is not recognized")


def gitlab_cicd(location: str, env: Environment, deploy_solution_slug: str):
    yaml = location + '/' + '.gitlab-ci.yml'
    template = env.get_template('.gitlab-ci.yml.jinja')

    with open(yaml, 'w') as f:
        f.write(template.render(
            deploy_solution=deploy_solution_slug
        ))

    print('Next steps:')
    print("""
1. Signing:
    - [Gitlab repository settings > CI/CD > Variables] Add variable as file KEYSTORE_FILE_BASE64
        > Get the base64-encoded content of your keystore:
        base64 -i <your.keystore>
    - [Gitlab repository settings > CI/CD > Variables] Add variable KEYSTORE_ALIAS
    - [Gitlab repository settings > CI/CD > Variables] Add variable KEYSTORE_PASSWORD (masked)""")
    if deploy_solution_slug == 'firebase-app-distribution':
        print("""
2. Firebase App Distribution
    - [.gitlab-ci.yml] Change variable FIREBASE_GROUPS of 'Deploy' job, if needed
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


def jenkins(location: str, env: Environment, deploy_solution_slug: str):
    jenkinsfile = location + '/' + 'Jenkinsfile'
    template = env.get_template('Jenkinsfile.jinja')

    with open(jenkinsfile, 'w') as f:
        f.write(template.render(
            deploy_solution=deploy_solution_slug
        ))

    print('Next steps:')
    print("""
1. Signing:
    - [Jenkins project > Credentials] Add credential as file KEYSTORE_FILE_BASE64
        > Get the base64-encoded content of your keystore:
        base64 -i <your.keystore>
    - [Manage Jenkins > Configure System] Add env variable KEYSTORE_ALIAS
    - [Jenkins project > Credentials] Add credential KEYSTORE_PASSWORD""")
    if deploy_solution_slug == 'firebase-app-distribution':
        print("""
2. Firebase App Distribution
    - [Jenkinsfile] Change variable groups of 'Deploy' job, if needed
    - [Jenkins project > Credentials] Add credential FIREBASE_TOKEN
        > Get your CI firebase token by running on your local machine:
        firebase login:ci
    - [Manage Jenkins > Configure System] Add env variable FIREBASE_APP_ID
        > Get the app id in Firebase project settings > General > Your apps
        > If you don't have any Firebase app registerd you can add one. You can get the certificate SHA-1/SHA-256 by running:
        keytool -list -v -keystore <your.keystore> -alias <alias>
        Enter keystore password
        Copy the SHA-1 or SHA-256 fingerprint
    - [Jenkins project > Credentials] Add credential as file FIREBASE_GOOGLE_SERVICES_JSON_FILE
        > Download the goog-services.json in Firebase project settings > General > Your apps
        > It is necessary to also have it on your local machine under app/ folder, but you should not commit this file""")

    print('\n👨🏻 Jenkinsfile')
