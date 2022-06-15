def get_slug_for(string: str):
    return string.lower().strip().replace(' ', '-').replace('_', '-').replace('/', '-')
