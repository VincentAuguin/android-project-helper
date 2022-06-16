from jinja2 import Environment


def add_gitlab_ci_cd(location: str, env: Environment, deploy_solution_slug: str):
    yaml = location + '/' + '.gitlab-ci.yml'
    template = env.get_template('.gitlab-ci.yml.jinja')

    with open(yaml, 'w') as f:
        f.write(template.render(
            deploy_solution=deploy_solution_slug
        ))

    _print_next_steps(deploy_solution_slug)
    print('\n🦊 .gitlab-ci.yml')


def _print_next_steps(deploy_solution_slug: str):
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
