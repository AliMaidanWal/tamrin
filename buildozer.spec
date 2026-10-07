[app]

# نام بازی
title = بازی حدس عدد

# نام بسته برنامه
package.name = guessnumber

# دامنه بسته
package.domain = org.alimaidanwal

# فایل اصلی بازی
source.dir = .

# فایل‌های مورد نیاز
source.include_exts = py,png,jpg,kv,atlas

# نسخه بازی
version = 1.0

# نیازمندی‌های Python
requirements = python3,kivy

# جهت صفحه
orientation = portrait

# تمام صفحه
fullscreen = 0


[buildozer]

# هشدارهای Buildozer
warn_on_root = 1

# لاگ
log_level = 2


[android]

# حداقل نسخه Android
android.minapi = 21

# نسخه هدف Android
android.api = 33

# معماری
android.archs = arm64-v8a

# اجازه اینترنت لازم نیست
android.permissions =

# نام فایل APK
android.entrypoint = org.kivy.android.PythonActivity
