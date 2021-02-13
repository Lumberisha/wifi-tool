import subprocess
import re
import numpy as np
import matplotlib.pyplot as plt


def calculate_strength_points(password):
    pattern = re.compile("[@_!#$%^&.,*()<>?/\|}{~:]")
    password_strength = 0
    lc = any(map(str.islower, password))
    upc = any(map(str.isupper, password))
    num = any(map(str.isdigit, password))
    spec = any(c in "[@_!#$%^&.,*()<>?/\|}{~:]" for c in password)

    if lc and upc and num and spec:
        password_strength += 50
        for x in password:
            if x.isdigit():
                password_strength += 1
            elif x.islower():
                password_strength += 2
            elif x.isupper():
                password_strength += 2
            elif pattern.search(password):
                password_strength += 4

    elif (num and lc and upc) or (num and lc and spec) or (num and upc and spec) or (lc and upc and spec):
        password_strength += 30
        for x in password:
            if x.isdigit():
                password_strength += 1
            elif x.islower():
                password_strength += 2
            elif x.isupper():
                password_strength += 2
            elif pattern.search(password):
                password_strength += 4
    elif (num and lc) or (num and upc) or (num and spec) or (lc and upc) or (lc and spec) or (upc and spec):
        password_strength += 20
        for x in password:
            if x.isdigit():
                password_strength += 1
            elif x.islower():
                password_strength += 2
            elif x.isupper():
                password_strength += 2
            elif pattern.search(password):
                password_strength += 4
    elif num or lc or upc:
        password_strength += 10
        for x in password:
            if x.isdigit():
                password_strength += 1
            elif x.islower():
                password_strength += 2
            elif x.isupper():
                password_strength += 2
            elif pattern.search(password):
                password_strength += 4
    return password_strength


command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()

profile_names = (re.findall("All User Profile     : (.*)\r", command_output))

wifi_list = list()
password_list = list()
password_strength_list = list()

if len(profile_names) != 0:
    for name in profile_names:
        wifi_profile = dict()
        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output=True).stdout.decode()
        if re.search("Security key           : Absent", profile_info):
            continue
        else:
            wifi_profile["WiFi"] = name
            profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"],
                                               capture_output=True).stdout.decode()
            password = re.search("Key Content            : (.*)\r", profile_info_pass)
            if password == None:
                wifi_profile["Password"] = None
            else:
                wifi_profile["Password"] = password[1]
                wifi_profile["Strength"] = calculate_strength_points(password[1])
            wifi_list.append(wifi_profile)
            password_list.append(password[1])
            password_strength_list.append(calculate_strength_points(password[1]))

for x in range(len(wifi_list)):
    print(wifi_list[x])

objects = tuple(password_list)
y_pos = np.arange(len(objects))

plt.bar(y_pos, password_strength_list)
plt.xticks(y_pos, objects, rotation=90)
plt.subplots_adjust(bottom=0.4)
plt.subplots_adjust(top=0.8)

plt.ylabel('Kompleksiteti')

plt.show()
