import shutil

from utils import args_utils


def raise_and_clean(msg: str, args: dict):
    location = args_utils.get_resolved_project_location(args)
    shutil.rmtree(location)
    raise RuntimeError(msg)
