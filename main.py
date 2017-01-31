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
from validation_helpers import valid_username, valid_password, valid_email

# html boilerplate for the top of every page
page_header = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>User Signup</title>
        <style type="text/css">
            .error {
                color: red;
                font-size: larger;
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

error_bad_username = ""
error_bad_password = ""
error_password_mismatch = ""
error_bad_email = ""

class Index(webapp2.RequestHandler):
    """
       Handles requests coming to "/", builds form
    """
    def get(self):
        page_header = "<h2>Create an account:</h2>"

        user_form = """
        <form action="/signup" method="post">
        <label>
            Username:
            <input type="text" name="username" />
        </label>
        """

        pass_form = """
        <br>
        <label>
            Password:
            <input type="password" name="password" />
        </label>
        """

        verify_pass_form = """
        <br>
        <label>
            Verify Password:
            <input type="password" name="verify_password" />
        </label>
        """

        email_form = """
        <br>
        <label>
            Email (optional):
            <input type="text" name="email" />
        </label>
        <br>
        <input type="submit" value="Sign me up!"/>
        """
        account_form = user_form + pass_form + verify_pass_form + email_form

        user_content = page_header + user_form + error_bad_username
        pass_content = pass_form + error_bad_password
        verify_pass_content = verify_pass_form + error_password_mismatch
        email_content = email_form + error_bad_email + page_footer

        content = user_content + pass_content + verify_pass_content + email_content

        self.response.write(content)

class Signup(webapp2.RequestHandler):
    """
       Handles requests coming to "/signup", validates data
    """
    def post(self):
        """
           Retrieve data entered, validate and sanitize
        """
        username_in = self.request.get("username")
        password_in = self.request.get("password")
        verify_password_in = self.request.get("verify_password")
        email_in = self.request.get("email")

        # validate username
        good_username = valid_username(username_in)

        if good_username:
            #sanitize username
            ok_username = cgi.escape(username_in, quote=True)
            error_bad_username = ""
        else:
            error_bad_username = "<span class='error'>Invalid username</span>"

        #validate password and compare against verify_password_in
        good_password = valid_password(password_in)

        if good_password:
            #make sure the passwords match
            error_bad_password = ""
            if password_in == verify_password_in:
                #sanitize password
                ok_password = cgi.escape(password_in,quote=True)
                good_match = True
                error_password_mismatch = ""
            else:
                good_match = False
                error_password_mismatch = """
                "<span class='error'>Passwords did not match</span>"
                """
        else:
            error_bad_password = "<span class='error'>Invalid password</span>"

        #validate email address
        good_email = valid_email(email_in)

        if good_email:
            #sanitize email
            ok_email = cgi.escape(email_in, quote=True)
            error_bad_email = ""
        else:
            error_bad_email = "<span class='error'>Invalid username</span>"

        if good_username and good_password and good_match and good_email:
            welcome_text = "<h1>Welcome, " + ok_username + "!</h1>"
            self.response.write(welcome_text)
        else:
            self.redirect("/")


class WelcomePage(webapp2.RequestHandler):
    """
       Handles requests coming to "/welcome", builds Welcome page
    """
    def get(self):
        welcome_text = "<h1>Welcome, " + ok_username + "!</h1>"
        self.response.write(welcome_text)

#app = webapp2.WSGIApplication([
#    ('/', Index),
#    ('/signup', Signup),
#    ('/welcome', WelcomePage)

app = webapp2.WSGIApplication([
    ('/', Index),
    ('/signup', Signup)
], debug=True)
