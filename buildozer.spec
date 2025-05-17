[app]

# (str) Title of your application
title = kisaan

# (str) Package name
package.name = kisaan

# (str) Package domain (reverse domain notation)
package.domain = org.kisaan

# (str) Source code where the main.py is located
source.dir = .

# (str) Application version
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Entry point file
source.main = main.py

# (str) Icon of the app
# icon.filename = %(source.dir)s/data/icon.png

# (list) Permissions (optional)
# android.permissions = INTERNET

[buildozer]

# (str) Path to the buildozer directory
build_dir = .buildozer

# (str) Android SDK path (overridden in your workflow)
android.sdk_path = ~/.buildozer/android/platform/android-sdk

# (str) Android NDK path (usually auto)
android.ndk_path = ~/.buildozer/android/platform/android-ndk

[android]

# (bool) Use --release flag to generate a signed APK
release = 1

# (str) Supported architectures
android.arch = arm64-v8a

# (str) Minimum API level supported
android.api = 34

# (str) Build tools version
android.build_tools_version = 34.0.0

# (str) Android NDK API level
android.ndk_api = 21

# Keystore details for signing
android.keystore = kisaan.keystore
android.keystore_password = your_keystore_password_here
android.keyalias = your_key_alias_here
android.key_password = your_key_password_here

# (bool) Copy library in APK or not
android.copy_libs = 1

# (str) Permissions
android.permissions = INTERNET

[log]

# (int) Log level
log_level = 2
