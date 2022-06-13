# Android Helper Project (APH)

This CLI aims to help you to initialize a new modern Android project with:

- Kotlin
- Compose
- Hilt

## Installation

Download the latest release of this repository and unzip the archive:
```bash
tar -xf aph.tar.gz
cd aph/
chmod +x ./aph
```

Ensure you have the environment variable `ANDROID_SDK_ROOT` set, if not:
```bash
export ANDROID_SDK_ROOT="/path/to/android/sdk"
```

## Usage

To create a project:
```bash
./aph create \
    --package-name=com.example.app
    --min-sdk-version=26 \
    "My awesome Android project" \
    /path/to/location
```

To get full available commands and options
```bash
./aph help
```

## Roadmap

- [x] `help` command
- [x] `create` command to initiate an Android app skeleton
- [ ] `add:module` command to add a module to an existing Android project
- [ ] `add:ci` command to add preformated CI file:
    - [ ] Gitlab CI/CD
    - [ ] Github Actions
    - [ ] Jenkins
    - [ ] Bitrise.io
    - [ ] Buddy.works
    - [ ] Docker (generate a `Dockerfile` to create the base image for CI agents to run from)

## Contribution

Feel free to contribute with pull requests :sunglasses: