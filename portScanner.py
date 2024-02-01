#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(15)


host = input("Please enter the IP you want to scan: ")
port = int(input("Enter the port you want to scan:" ))


def PortScanner(port):
    if s.connect_ex((host, port)):
        print("The port is closed")

    else:
        print("The port is open")

PortScanner(port)