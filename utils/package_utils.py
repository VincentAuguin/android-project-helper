import os
import re


def create_package_directories(location: str, package_name: str):
    packages = location + "/" + package_name.replace('.', '/')
    os.makedirs(packages)
    return packages


def find_package_name(location: str):
    manifest = f"{location}/app/src/main/AndroidManifest.xml"
    pattern = r"package=\"((?:\w+\.)+(?:\w+))\""
    f = open(manifest, 'r')
    return re.findall(pattern, string=f.read(), flags=re.MULTILINE)[0]
