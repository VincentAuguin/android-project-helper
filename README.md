# Android Helper Project (APH)

This CLI aims to help you to initialize a new modern Android project with:

- Kotlin
- Compose
- Hilt

## Installation

Download the latest release of this repository and unzip the archive to get `aph` binary.

## Usage

Remember to make the binary executable:
```bash
chmod +x ./aph
```

Ensure you have the environment variable `ANDROID_SDK_ROOT` set, if not:
```bash
export ANDROID_SDK_ROOT="/path/to/android/sdk"
```

To create a project:
```bash
./aph create \
    --package-name=com.example.app
    --min-sdk-version=26 \
    "My awesome Android project" \
    /path/to/location
```

## Contribution

Feel free to contribute with pull requests :sunglasses: