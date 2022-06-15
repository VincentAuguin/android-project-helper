FROM gradle:jdk11

USER root

ENV SDK_URL "https://dl.google.com/android/repository/commandlinetools-linux-8092744_latest.zip"
ENV ANDROID_HOME "/usr/local/android-sdk"
ENV ANDROID_SDK_ROOT "${ANDROID_HOME}"
ENV ANDROID_CMDLINE_TOOLS "${ANDROID_HOME}/cmdline-tools/latest"
ENV PATH "${ANDROID_CMDLINE_TOOLS}/emulator:${ANDROID_CMDLINE_TOOLS}/bin:${ANDROID_CMDLINE_TOOLS}/tools:${ANDROID_CMDLINE_TOOLS}/tools/bin:${ANDROID_CMDLINE_TOOLS}/platform-tools:/opt/firebase/bin:${PATH}"
ENV ANDROID_VERSION 32
ENV BUILD_TOOLS_VERSION '32.0.0'

RUN apt-get update \
    && apt-get install build-essential -y \
    && apt-get install file -y \
    && apt-get install apt-utils -y \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p "$ANDROID_HOME/.android" \
    && cd $ANDROID_HOME \
    && curl -o sdk.zip $SDK_URL \
    && mkdir cmdline-tools \
    && unzip sdk.zip -d cmdline-tools > /dev/null \
    && mv cmdline-tools/cmdline-tools cmdline-tools/latest \
    && rm sdk.zip \
    && mkdir "$ANDROID_HOME/licenses" || true \
    && chmod -R 777  $ANDROID_HOME \
    && mkdir ~/.android \
    && echo '### User Sources for Android SDK Manager' > ~/.android/repositories.cfg \
    && yes | sdkmanager --licenses > /dev/null \
    && yes | sdkmanager --update \
    && sdkmanager "platforms;android-${ANDROID_VERSION}" \
    && sdkmanager "build-tools;${BUILD_TOOLS_VERSION}"

RUN mkdir -p /opt/firebase/bin \
    && wget -O /opt/firebase/bin/firebase_tools "https://firebase.tools/bin/linux/latest" > /dev/null \
    && chmod +x /opt/firebase/bin/firebase_tools \
    && echo 'alias firebase="firebase_tools"' >> ~/.bash_aliases

USER gradle