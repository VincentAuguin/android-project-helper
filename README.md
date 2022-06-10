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

## Contribution

Feel free to contribute with pull requests :sunglasses: