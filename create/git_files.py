from jinja2 import Environment


def create(root: str, env: Environment):
    print('🛠 Git files...')

    create_git_ignore(root, env)


def create_git_ignore(root: str, env: Environment):
    gitignore = root + '/' + '.gitignore'
    template = env.get_template('.gitignore.jinja')
    with open(gitignore, 'w') as f:
        f.write(template.render())

    print('📄 .gitignore')
