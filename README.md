# Android Helper Project (APH)

This CLI aims to help you wrapping up your Android project quickly.

[![asciicast](https://asciinema.org/a/E91ADazWP2qHvZ11nXSgFeZWg.svg)](https://asciinema.org/a/E91ADazWP2qHvZ11nXSgFeZWg?speed=3)

## Installation (MacOs/Linux only)

### Homebrew

```bash
brew tap vincentauguin/cli
brew install aph
```

### Manually

Download the latest release of this repository and unzip the archive:
```bash
tar -xf aph.tar.gz
chmod +x ./aph
cp aph /usr/local/bash # or whatever directory in your $PATH
```

## Usage

### Create project

You need to have the env variable `ANDROID_SDK_ROOT` set, if not:

```bash
# ZSH
echo 'export ANDROID_SDK_ROOT=path/to/sdk/location' >> ~/.zshenv && source ~/.zshenv
# Bash
echo 'export ANDROID_SDK_ROOT=path/to/sdk/location' >> ~/.bash_profile && source ~/.bash_profile
```

Then, to create a project:
```bash
aph create \
    --package-name=com.example.app
    --min-sdk-version=26 \
    "My awesome Android project" \
    /path/to/location
```

### Add module

To add a new module to an existing project:
```bash
aph add:module /path/to/android/project
```

### Add CI solution

To build and deploy your app with automated CI:
```bash
aph add:ci
```

See the current supported solutions in [Roadmap](#Roadmap) section.

### Help

To get full available commands and options
```bash
aph help
```

## Roadmap

- [x] `help` command
- [x] `create` command to initiate an Android app skeleton
- [x] `add:module` command to add a module to an existing Android project
- [x] `add:ci` command to add preformated CI solution:
    - [x] Gitlab CI/CD
    - [ ] Github Actions
    - [x] Jenkins
    - [x] Bitrise.io
    - [ ] Buddy.works

## Contributing

Feel free to contribute with pull requests :sunglasses:

### Develop from sources

```bash
# Binary dependencies
brew install python@3.9 gradle
# Python dependencies
pip3 install jinja2 inquirer docopt
# Run from source
python3 aph.py <command>
```

### Bundle it

```bash
# Install pyinstaller to bundle our python app
pip3 install pyinstaller
# Bundle it
pyinstaller \
--add-data add_ci/templates:add_ci/templates \
--add-data create/templates:create/templates \
--add-data add_module/templates:add_module/templates \
--target-architecture universal2 \
--onefile aph.py
# Test the generated bundle
cd dist
./aph <command>
```

### Distribute it

Create a Tag according to SemVer `X.Y.Z` and create the associated Release on this repository. Upload the archived binary:

```bash
tar -czvf aph.tar.gz aph
```

Get the SHA-256 signature to update [homebrew formula](https://github.com/VincentAuguin/homebrew-cli/blob/main/Formula/aph.rb):

```bash
shasum -a 256 aph.tar.gz
```