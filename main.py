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

def page_html(
    bad_user,
    bad_pass,
    bad_pass_verify,
    bad_email,
    user_in,
    email_in
    ):

    account_form = """
    <h2>Create an account:</h2>
    <form action="/signup" method="post">
        <table>
            <tbody>
                <tr>
                    <td class="label">
                        Username:
                    </td>
                    <td>
                        <input type="text" name="username" value="%s" />
                    </td>
                    <td class="error">%s</td>
                </tr>
                <tr>
                    <td class="label">
                        Password:
                    </td>
                    <td>
                        <input type="password" name="password" />
                    </td>
                    <td class="error">%s</td>
                </tr>
                <tr>
                    <td class ="label">
                        Verify Password:
                    </td>
                    <td>
                        <input type="password" name="verify_password" />
                    </td>
                    <td class="error">%s</td>
                </tr>
                <tr>
                    <td class ="label">
                        Email (optional):
                    </td>
                    <td>
                        <input type="text" name="email" value="%s" />
                    </td>
                    <td class="error">%s</td>
                </tr>
            </tbody>
        </table>

        <input type="submit" value="Sign me up!"/>
        """ % (user_in, bad_user, bad_pass, bad_pass_verify, email_in, bad_email)

    content = page_header + account_form + page_footer
    return content

class Index(webapp2.RequestHandler):
    """
       Handles requests coming to "/", builds form
    """

    def get(self):
        """ provides the HTML for the sign up """
        bad_user = ""
        bad_pass = ""
        bad_pass_verify = ""
        bad_email = ""
        user = ""
        email = ""

        content = page_html(
        bad_user,
        bad_pass,
        bad_pass_verify,
        bad_email,
        user,
        email
        )

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
            err_username = ""
        else:
            err_username = "Invalid username"

        #validate password and compare against verify_password_in
        good_password = valid_password(password_in)

        if good_password:
            #make sure the passwords match
            err_password = ""
            if password_in == verify_password_in:
                #sanitize password
                ok_password = cgi.escape(password_in,quote=True)
                good_match = True
                err_password_mismatch = ""
            else:
                good_match = False
                err_password_mismatch = "Passwords did not match"
        else:
            err_password = "Invalid password"
            err_password_mismatch = ""

        #validate email address
        good_email = valid_email(email_in)

        if good_email or email_in == "" :
            #sanitize email
            ok_email = cgi.escape(email_in, quote=True)
            err_email = ""
        else:
            err_email = "Invalid email"

        if (good_username
        and good_password
        and good_match
        and (good_email or email_in == "")):
            #welcome_text = "<h1>Welcome, " + ok_username + "!</h1>"
            self.redirect("/welcome?username=" + ok_username)
        else:
            content = page_html(
            err_username,
            err_password,
            err_password_mismatch,
            err_email,
            username_in,
            email_in
            )
            self.response.write(content)
            #self.redirect("/")


class WelcomePage(webapp2.RequestHandler):
    """
       Handles requests coming to "/welcome", builds Welcome page
    """
    def get(self):
        username = self.request.get('username')
        if valid_username(username):
            welcome_text = "<h1>Welcome, " + username + "!</h1>"
            self.response.write(welcome_text)
        else:
            self.redirect('/signup')

app = webapp2.WSGIApplication([
    ('/', Index),
    ('/signup', Signup),
    ('/welcome', WelcomePage)

], debug=True)
