# CthePrez CookieHTTPGet 3/4/2016
# Learning to authenticate with a web interface on a switch that requires a non-standard cookie
##############################
# HTTP Get String used for authenticating with a specific device.  This is the basic part, however cookies will have to be handled.  
# "GET / HTTP/1.1\r\nHost: " + host_IP + "\r\nConnection:" + con_Type + "\r\nAuthorization: " + auth_Type + key_Base64 +"\r\n\r\n"
# key_Base64 = Base64 encoding of "username:password"
#
# Collect Usr/Pwd > Build String > Encode String ? Build HTTP String > Send HTTP String >
# Recieve Results > Parse Results > Handle Cookies > ??? > Access!
# 

import base64
import sys
import socket

host_IP = "127.0.0.1"
con_Type = "close"
auth_Type = "Basic"
key_Base64 = base64.b64encode("username:password".encode('utf-8'))

print(key_Base64.decode('utf-8'))
