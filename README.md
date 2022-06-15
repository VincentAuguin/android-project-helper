# Android Helper Project (APH)

This CLI aims to help you to initialize a new modern Android project with:

- Kotlin
- Compose
- Hilt

It also helps with CI integration.

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

### Create project

To create a project:
```bash
./aph create \
    --package-name=com.example.app
    --min-sdk-version=26 \
    "My awesome Android project" \
    /path/to/location
```

### Add CI solution

To build and deploy your app with automated CI:
```bash
./aph ci
```

See the current supported solutions in [Roadmap](#Roadmap) section.

### Help

To get full available commands and options
```bash
./aph help
```

## Roadmap

- [x] `help` command
- [x] `create` command to initiate an Android app skeleton
- [ ] `add:module` command to add a module to an existing Android project
- [x] `add:ci` command to add preformated CI solution:
    - [x] Gitlab CI/CD
    - [ ] Github Actions
    - [ ] Jenkins
    - [ ] Bitrise.io
    - [ ] Buddy.works

## Contribution

Feel free to contribute with pull requests :sunglasses: