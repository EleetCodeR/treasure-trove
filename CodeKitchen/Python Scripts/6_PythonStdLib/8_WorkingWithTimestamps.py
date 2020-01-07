import time


def send_emails():
    for i in range(10000):
        pass


# Time method returns timestamps in seconds. (time from the start of the windows-sys epoch till the call)
start = time.time()
send_emails()
end = time.time()
duration = start-end
print(duration)
