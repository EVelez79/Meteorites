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
import webapp2
import jinja2
import os
import json

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
    loader = jinja2.FileSystemLoader(template_dir))
env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render())

class GlobeHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('globe.html')
        self.response.out.write(template.render())

class MapHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('map.html')
        self.response.out.write(template.render())

class UpdatesHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('updates.html')
        self.response.out.write(template.render())


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/globe', GlobeHandler),
    ('/map', MapHandler),
    ('/updates', UpdatesHandler),
], debug=True)
