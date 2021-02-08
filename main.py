import re
import threading
import subprocess

import tkinter as tk

window = tk.Tk()


def start():
    command1 = "netsh wlan show profile"
    network = subprocess.run(command1, shell=True, capture_output=True, text=True)
    net_op = network.stdout

    pw_list = []

    pattern = re.compile(r"(Profile\s*:\s)(.*)")
    matches = pattern.finditer(net_op)
    for match in matches:

        net_name = match.group(2)
        command2 = "netsh wlan show profile " + '"' + net_name + '"' + " key=clear"
        net_info = subprocess.run(command2, shell=True, capture_output=True, text=True)

        pattern2 = re.compile(r"(SSID name\s*:\s)(.*)")
        wlan_name = pattern2.finditer(net_info.stdout)
        pass_pattern = re.compile(r"(Key Content\s*:\s)(.*)")
        pass_match = pass_pattern.finditer(net_info.stdout)

        for wname, passwd in zip(wlan_name, pass_match):
            pw_list.append(passwd.group(2))

    def checker(input):
        pattern = "!@#$%^&*()-+?_=,<>/"

        lc = any(map(str.islower, input))
        uc = any(map(str.isupper, input))
        num = any(map(str.isdigit, input))
        spec = any(c in pattern for c in input)
        length = len(input) > 7

        if lc and uc and num and spec and length:
            greeting = tk.Label(text=input + " > EXPERT")
            greeting.pack()

        elif length and lc and num and spec:
            greeting = tk.Label(text=input + " > HARD")
            greeting.pack()

        elif length and uc and num and spec:
            greeting = tk.Label(text=input + " > HARD")
            greeting.pack()

        elif length and lc and uc and num:
            greeting = tk.Label(text=input + " > MEDIUM")
            greeting.pack()

        elif length and lc and num:
            greeting = tk.Label(text=input + " > MEDIUM")
            greeting.pack()

        elif length or num or lc or uc:
            greeting = tk.Label(text=input + " > EASY")
            greeting.pack()

    for pw in pw_list:
        checker(pw)


startButton = tk.Button(
    window, text="START", command=threading.Thread(target=start).start()
)

startButton.pack()


window.geometry("400x400")


window.mainloop()
