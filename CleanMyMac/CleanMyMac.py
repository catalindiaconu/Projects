# source: https://macpaw.com/how-to/delete-junk-files-on-mac
import os
import getpass

# passwd = getpass.getpass()


def delete_caches():
    print("\nLocation: ~/Library/Caches")
    caches_location = os.path.expanduser("~/Library/Caches/")  # used to allow the use of tilde (~) sign
    caches_objects = os.listdir(caches_location)
    f = open("log.txt", "a")
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
    for i in languages_objects:
        os.system("du -hs {}{}/Contents/Resources".format(languages_location, i))
        # os.system("ls -al {}{}/Contents/Resources/*.lproj".format(languages_location, i))


# delete_caches()
# delete_user_logs()
delete_languages()
