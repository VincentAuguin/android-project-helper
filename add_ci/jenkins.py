from jinja2 import Environment


def add_jenkins(location: str, env: Environment, deploy_solution_slug: str):
    jenkinsfile = location + '/' + 'Jenkinsfile'
    template = env.get_template('Jenkinsfile.jinja')

    with open(jenkinsfile, 'w') as f:
        f.write(template.render(
            deploy_solution=deploy_solution_slug
        ))

    _print_next_steps(deploy_solution_slug)
    print('\n👨🏻 Jenkinsfile')


def _print_next_steps(deploy_solution_slug: str):
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
