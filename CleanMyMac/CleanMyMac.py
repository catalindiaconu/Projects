# source: https://macpaw.com/how-to/delete-junk-files-on-mac
import os
import getpass

passwd = getpass.getpass()


def delete_caches():
    print("\nLocation: ~/Library/Caches")
    caches_location = os.path.expanduser("~/Library/Caches/")  # used to allow the use of tilde (~) sign
    caches_objects = os.listdir(caches_location)
    for i in caches_objects:
        os.system("echo {} | sudo -S rm -rf {}{}".format(passwd, caches_location, i))
        print("deleting: {}".format(i))


def delete_user_logs():
    print("\nLocation: ~/Library/Logs")
    logs_location = os.path.expanduser("~/Library/Logs/")
    logs_objects = os.listdir(logs_location)
    for i in logs_objects:
        os.system("echo {} | sudo -S rm -rf {}{}".format(passwd, logs_location, i))
        print("deleting: {}".format(i))


def delete_languages():
    languages_location = "/System/Applications/"
    languages_objects = os.listdir(languages_location)
    os.system("du -hs {}*.app/Contents/Resources".format(languages_location))
    # os.system("find {}*.app/Contents/Resources -name '*.lproj' -type d -not -path '{}*.app/Contents/Resources/en*' -exec rm -rf {} \;".format(languages_location, languages_location))


delete_caches()
delete_user_logs()
# delete_languages()
# Errors reported:
# - Operation not permitted (even with SUDO): SIP must be disabled.
# - Read-only file system: even with SIP disabled. Because the files are stored on /
# Plus the space taken by the files is not that big.
