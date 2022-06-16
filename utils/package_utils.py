import os


def create_package_directories(location: str, package_name: str):
    packages = location + "/" + package_name.replace('.', '/')
    os.makedirs(packages)
    return packages
