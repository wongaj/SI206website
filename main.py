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
import os
import logging
import jinja2

# Lets set it up so we know where we stored the template files
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class IndexHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("GET")
        templatestring = 'templates'
        pathstring = self.request.path
        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        if pathstring == "/index.html":
            self.response.write(template.render({'title': 'Alden Wong', 'title2':'Home', 'Home':'HOME', 'Family':'Family', 'Food':'Food', 'Login':'Login'}))
        elif pathstring == "/family.html":
            template = JINJA_ENVIRONMENT.get_template(templatestring+pathstring)
            self.response.write(template.render({'title': 'Family', 'Home':'Home', 'Family':'FAMILY', 'Food':'Food', 'Login':'Login'}))
        elif pathstring == "/food.html":
            template = JINJA_ENVIRONMENT.get_template(templatestring+pathstring)
            self.response.write(template.render({'title': 'Food', 'Home':'Home', 'Family':'Family', 'Food':'FOOD', 'Login':'Login'}))
        else:
            self.response.write(template.render({'title': 'Alden Wong', 'title2':'Home', 'Home':'HOME', 'Family':'Family', 'Food':'Food', 'Login':'Login'}))
                

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("GET")
        template = JINJA_ENVIRONMENT.get_template('templates/login.html')
        self.response.write(template.render({'title': 'Login', 'Home':'Home', 'Family':'Family', 'Food':'Food', 'Login':'LOGIN'}))
    def post(self):   
        logging.info("POST")
        username = self.request.get('name')
        userpass = self.request.get('pw')
        if username == 'Colleen' and userpass == 'pass':
            template = JINJA_ENVIRONMENT.get_template('templates/success.html')
            self.response.write(template.render({'title': 'Logged in...', 'Home':'Home', 'Family':'Family', 'Food':'Food', 'Login':'LOGIN', 'message':'You have successfully logged in!! Way to go!'}))
            logging.info("correct input")
        else:
            template = JINJA_ENVIRONMENT.get_template('templates/login.html')
            self.response.write(template.render({'title': 'Login', 'Home':'Home', 'Family':'Family', 'Food':'Food', 'Login':'LOGIN', 'message':'Bad credentials. Try again.'}))
            logging.info("incorrect input. try again")

app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/index.html', IndexHandler),
    ('/family.html', IndexHandler),
    ('/food.html', IndexHandler),
    ('/login.html', LoginHandler),
    ('success.html', LoginHandler)
], debug=True)
