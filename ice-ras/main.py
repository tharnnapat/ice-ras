#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License 
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
import jinja2
import webapp2
from google.appengine.api import rdbms


JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])

_INSTANCE_NAME="prinya-th-2013:prinya-db"

class Notification(webapp2.RequestHandler):
	def get(self):

		conn = rdbms.connect(instance=_INSTANCE_NAME, database='Prinya_Project')
	    	cursor = conn.cursor()
	    	sql = ("""select log_id,course_name,day,time,l.type,l.staff_id,firstname,email 
					from log l join staff s 
					on l.staff_id=s.staff_id 
					join course c
					on c.course_id=l.course_id
					order by log_id desc""")
		cursor.execute(sql)

		templates = {

					'log' : cursor.fetchall(),

					}

		template = JINJA_ENVIRONMENT.get_template('notification.html')
		self.response.write(template.render(templates))
			
		# conn.close();

app = webapp2.WSGIApplication([
    ('/', Notification),
], debug=True)
