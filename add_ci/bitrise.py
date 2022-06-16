from jinja2 import Environment


def add_bitrise(location: str, env: Environment, deploy_solution_slug: str):
    yaml = location + '/' + 'bitrise.yml'
    template = env.get_template('bitrise.yml.jinja')

    with open(yaml, 'w') as f:
        f.write(template.render(
            deploy_solution=deploy_solution_slug
        ))

    _print_next_steps(deploy_solution_slug)
    print('\n🤖 bitrise.yml')


def _print_next_steps(deploy_solution_slug: str):
    print('Next steps:')
    print("""
1. Signing:
    - [Bitrise project > Workflow > Code Signing > Android Keystore File] Fill out section
        > Upload your keystore file
        > Fill out password, alias and private key password fields""")
    if deploy_solution_slug == 'firebase-app-distribution':
        print("""
2. Firebase App Distribution
    - [bitrise.yml] Change parameter 'groups' of step 'firebase-app-distribution', if needed
    - [Bitrise project > Workflow > Secrets] Add secret FIREBASE_TOKEN
        > Get your CI firebase token by running on your local machine:
        firebase login: ci
    - [Bitrise project > Workflow > Env Vars] Add variable FIREBASE_APP_ID
        > Get the app id in Firebase project settings > General > Your apps
        > If you don't have any Firebase app registerd you can add one. You can get the certificate SHA-1/SHA-256 by running:
        keytool -list -v -keystore <your.keystore> -alias <alias>
        Enter keystore password
        Copy the SHA-1 or SHA-256 fingerprint
    - [Bitrise project > Workflow > Code Signing > Generic File Storage] Upload your google-services.json with file storage id 'FIREBASE_GOOGLE_SERVICES_JSON'
        > Download the goog-services.json in Firebase project settings > General > Your apps
        > It is necessary to also have it on your local machine under app/ folder, but you should not commit this file
    - [bitrise.yml] It may happen that deployment requires service account usage. If so you can follow the instructions of step 'firebase-app-distribution' for commented input 'service_credentials_file'""")
