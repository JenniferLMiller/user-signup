#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
import re

username_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
password_RE = re.compile(r"^.{3,20}$")
email_RE = re.compile(r"^[\S]+[\S]+.[\S]+$")

# html boilerplate for the top of every page
page_header = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>User Signup</title>
        <style type="text/css">
            .error {
                color: red;
                }
        </style>
    </head>
    <body>
        <h1>
            <a href="/">User Signup</a>
        </h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
    </body>
    </html>
    """
def valid_username(username):
    return username_RE.match(username)

def valid_password(password):
    return password_RE.match(password)

def valid_email(email):
    return email_RE.match(email)

class Index(webapp2.RequestHandler):
    """
       Handles requests coming to "/", builds form
    """
    def get(self):
        page_header = "<h2>Create an account:</h2>"

        account_form = """
        <form action="/signup" method="post">
        <label>
            Username:
            <input type="text" name="username" />
        </label>
        <br>
        <label>
            Password:
            <input type="password" name="password" />
        </label>
        <br>
        <label>
            Verify Password:
            <input type="password" name="verify_password" />
        </label>
        <br>
        <label>
            Email (optional):
            <input type="text" name="email" />
        </label>
        <br>
        <input type="submit" value="Sign me up!"/>
        """
        content = page_header + account_form + page_footer
        self.response.write(content)

class Signup(webapp2.RequestHandler):
    """
       Handles requests coming to "/signup", validates data
    """
    def post(self):
        #"""
        #   Retrieve data entered, validate and sanitize
        #"""
        username_in = self.request.get("username")
        password_in = self.request.get("password")
        verify_password_in = self.request.get("verify_password")
        email_in = self.request.get("email")

        #good_username = valid_username(username_in)
        #good_password = valid_password(password_in)
        #good_email = valid_email(email_in)

class WelcomePage(webapp2.RequestHandler):
    """
       Handles requests coming to "/welcome", builds Welcome page
    """
    def get(self):
        username = "Jen"   ## temporary!
        welcome_text = "<h1>Welcome, " + username + "!</h1>"
        self.response.write(welcome_text)

app = webapp2.WSGIApplication([
    ('/', Index),
    ('/signup', Signup),
    ('/welcome', WelcomePage)
], debug=True)
