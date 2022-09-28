#!/usr/bin/env python3

import cgi
import os
from templates import after_login_incorrect, login_page
from templates import secret_page
import secret

def parse_cookies(cookie_string):
    cookies = cookie_string.split(';')
    result = {}
    for cookie in cookies:
        split_cookie =  cookie.split('=')
        result[split_cookie[0]] = split_cookie[1]

    return result

form = cgi.FieldStorage()

username = form.getfirst("username")
password = form.getfirst("password")

# check if login good
goodlogin = False
if username == secret.username and password == secret.password:
    goodlogin = True

cookies = parse_cookies(os.environ["HTTP_COOKIE"])

cookie_username = None
cookie_password = None

if cookies.get("username"):
    cookie_username = cookies.get("username").value
    
if cookies.get("password"):
    cookie_username = cookies.get("password").value

# check if cookie good
goodcookie = False
if cookie_username == secret.username and cookie_password == secret.password:
    goodcookie = True

if goodcookie:
    username = cookie_username
    password = cookie_password

print("Content-Type: text/html")


if goodlogin:
    print("Set-Cookie: username={username}")
    print("Set-Cookie: password={password}")
print()

if not username and not password:
    print(login_page())

elif username == secret.username and password == secret.password:
    print(secret_page(username,password))

else:
    print(after_login_incorrect())
