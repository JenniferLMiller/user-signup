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


class Index(webapp2.RequestHandler):
    """
       Handles requests coming to "/", builds form
    """
    def get(self):
        page_header = "<h2>Create an account:</h2>"

        account_form = """
        <form action="/" method="post">
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
        """
        self.response.write(page_header + account_form + page_footer)

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
    ('/welcome', WelcomePage)
], debug=True)
