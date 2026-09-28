[app]
title = Telekom Ombor
package.name = telekomombor
package.domain = org.telekom.ombor
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,xlsx
requirements = python3,kivy==2.3.0,openpyxl
version = 1.0
permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 24
android.archs = arm64-v8a
p4a.branch = master
android.accept_sdk_license = True
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1
