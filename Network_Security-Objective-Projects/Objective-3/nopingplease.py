#!/usr/bin/env python
# -*- coding: utf-8 -*-

# No Ping Please is used to block and allow ICMP echo replies.
# This means whenever another machine tries to PING this machine it will time out.
# This script requires colorama to run, use "pip install colorama" to install it.
# This script requires SUDO privileges to run correctly.

import os
import string
from colorama import *
#print(Fore.RED + 'some red text')
#print(Back.WHITE + Style.BRIGHT + Fore.RED + "" + Style.RESET_ALL)

def menu():
    choice = 3
    while choice != 0:
        print(Back.WHITE + Style.BRIGHT + Fore.RED + "=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+" + Style.RESET_ALL)
        print(Back.WHITE + Style.BRIGHT + Fore.RED + "|                                                                                      |" + Style.RESET_ALL)
        print(Back.WHITE + Style.BRIGHT + Fore.RED + "|   ▄   ████▄     █ ▄▄  ▄█    ▄     ▄▀      █ ▄▄  █     ▄███▄   ██      ▄▄▄▄▄   ▄███▄  |" + Style.RESET_ALL)
        print(Back.WHITE + Style.BRIGHT + Fore.RED + "|    █  █   █     █   █ ██     █  ▄▀        █   █ █     █▀   ▀  █ █    █     ▀▄ █▀   ▀ |" + Style.RESET_ALL)
        print(Back.WHITE + Style.BRIGHT + Fore.RED + "|██   █ █   █     █▀▀▀  ██ ██   █ █ ▀▄      █▀▀▀  █     ██▄▄    █▄▄█ ▄  ▀▀▀▀▄   ██▄▄   |" + Style.RESET_ALL)
        print(Back.WHITE + Style.BRIGHT + Fore.RED + "|█ █  █ ▀████     █     ▐█ █ █  █ █   █     █     ███▄  █▄   ▄▀ █  █  ▀▄▄▄▄▀    █▄   ▄▀|" + Style.RESET_ALL)
        print(Back.WHITE + Style.BRIGHT + Fore.RED + "|█  █ █            █     ▐ █  █ █  ███       █        ▀ ▀███▀      █            ▀███▀  |" + Style.RESET_ALL)
        print(Back.WHITE + Style.BRIGHT + Fore.RED + "|█   ██             ▀      █   ██             ▀                   █                    |" + Style.RESET_ALL)
        print(Back.WHITE + Style.BRIGHT + Fore.RED + "|                                                                ▀                     |" + Style.RESET_ALL)
        print(Back.WHITE + Style.BRIGHT + Fore.RED + "+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=" + Style.RESET_ALL)
        print(Back.WHITE + Style.BRIGHT + Fore.RED + "| No Ping Please is used to block and allow ICMP echo replies.                         |" + Style.RESET_ALL)
        print(Back.WHITE + Style.BRIGHT + Fore.RED + "| This means whenever another machine tries to PING this machine it will time out.     |" + Style.RESET_ALL)
        print(Back.WHITE + Style.BRIGHT + Fore.RED + "| This script requires SUDO privileges to run correctly.                               |" + Style.RESET_ALL)
        print(Back.WHITE + Style.BRIGHT + Fore.RED + "|                                                                                      |" + Style.RESET_ALL)
        print(Back.WHITE + Style.BRIGHT + Fore.RED + "| Main Menu:                                                                           |" + Style.RESET_ALL)
        print(Back.WHITE + Style.BRIGHT + Fore.RED + "| 0. Exit No Ping Please                                                               |" + Style.RESET_ALL)
        print(Back.WHITE + Style.BRIGHT + Fore.RED + "| 1. Disable ICMP Echo Replies                                                         |" + Style.RESET_ALL)
        print(Back.WHITE + Style.BRIGHT + Fore.RED + "| 2. Enable ICMP Echo Replies                                                          |" + Style.RESET_ALL)
        print(Back.WHITE + Style.BRIGHT + Fore.RED + "+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=" + Style.RESET_ALL)
        choice = input(Back.WHITE + Style.BRIGHT + Fore.RED + "Enter Choice:> ")
        if choice == 1:
            check = ["net.ipv4.icmp_echo_ignore_all = 1"]
            print(Back.WHITE + Style.BRIGHT + Fore.RED + "| Disabling ICMP Echo Replies...                                                       |" + Style.RESET_ALL)
            config = open("/etc/sysctl.conf", "r")
            inside = config.readlines()
            insideString = " ".join([str(line) for line in inside])
            if any(line in insideString for line in check):
                print(Back.WHITE + Style.BRIGHT + Fore.RED + "| ICMP Echo Replies already disabled...                                                |" + Style.RESET_ALL)
                print(Back.WHITE + Style.BRIGHT + Fore.RED + "| Redirecting To Main Menu...                                                          |" + Style.RESET_ALL)
                config.close()
            else:
                inside2 = config.readlines()
                config.close()
                inside2String = "\n".join([str(elem) for elem in inside2])
                inside2String.replace("net.ipv4.icmp_echo_ignore_all = 0", "")
                newConfig = open("/etc/sysctl1.conf", "a")
                newConfig.write(inside2String)
                newConfig.close()
                os.system("rm /etc/sysctl.conf")
                os.system("mv /etc/sysctl1.conf /etc/sysctl.conf")
                os.system("sysctl -p")                
                configWrite = open("/etc/sysctl.conf", "a")
                configWrite.write("net.ipv4.icmp_echo_ignore_all = 1")
                configWrite.close()
                os.system("sysctl -p")
                print(Back.WHITE + Style.BRIGHT + Fore.RED + "| ICMP Echo Replies disabled...                                                        |" + Style.RESET_ALL)
                print(Back.WHITE + Style.BRIGHT + Fore.RED + "| Redirecting To Main Menu...                                                          |" + Style.RESET_ALL)
            choice = 3
                    
        elif choice == 2:
            check = ["net.ipv4.icmp_echo_ignore_all = 1"]
            print(Back.WHITE + Style.BRIGHT + Fore.RED + "| Enabling ICMP Echo Replies...                                                        |" + Style.RESET_ALL)
            config = open("/etc/sysctl.conf", "r")
            inside = config.readlines()
            insideString = " ".join([str(line) for line in inside])
            if any(line in insideString for line in check):
                inside2 = config.readlines()
                config.close()
                inside2String = "\n".join([str(elem) for elem in inside2])
                inside2String.replace("net.ipv4.icmp_echo_ignore_all = 1", "")
                newConfig = open("/etc/sysctl1.conf", "a")
                newConfig.write(inside2String)
                newConfig.close()
                os.system("rm /etc/sysctl.conf")
                os.system("mv /etc/sysctl1.conf /etc/sysctl.conf")
                os.system("sysctl -p")
                enablePing = open("/etc/sysctl.conf", "a")
                enablePing.write("net.ipv4.icmp_echo_ignore_all = 0")
                enablePing.close()
                os.system("sysctl -p")                
                print(Back.WHITE + Style.BRIGHT + Fore.RED + "| ICMP Echo Replies enabled...                                                         |" + Style.RESET_ALL)
                print(Back.WHITE + Style.BRIGHT + Fore.RED + "| Redirecting To Main Menu...                                                          |" + Style.RESET_ALL)
            else:
                print(Back.WHITE + Style.BRIGHT + Fore.RED + "| ICMP Echo Replies already enabled...                                                 |" + Style.RESET_ALL)
                print(Back.WHITE + Style.BRIGHT + Fore.RED + "| Redirecting To Main Menu...                                                          |" + Style.RESET_ALL)
                config.close()
            choice = 3
            
    print(Back.WHITE + Style.BRIGHT + Fore.RED + "| Exiting...                                                                          |" + Style.RESET_ALL)
    exit()

menu()
