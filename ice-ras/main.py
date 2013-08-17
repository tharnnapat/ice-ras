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
from datetime import datetime
from pytz import timezone
import pytz

JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])

_INSTANCE_NAME="prinya-th-2013:prinya-db"
# class MainHandler(webapp2.RequestHandler):
# 	def get(self):

# 		conn = rdbms.connect(instance=_INSTANCE_NAME, database='Prinya_Project')
#     		cursor = conn.cursor()
# 		cursor.execute('SELECT course_id,course_code,course_name,credit_lecture,credit_lab,credit_learning,status FROM course natural join regiscourse')

# 		conn2=rdbms.connect(instance=_INSTANCE_NAME, database='Prinya_Project')
#     		cursor2 = conn2.cursor()
# 		cursor2.execute('SELECT sum(capacity),sum(enroll) FROM section group by regiscourse_id')

# 		# conn3=rdbms.connect(instance=_INSTANCE_NAME, database='Prinya_Project')
#   #   		cursor3 = conn3.cursor()
# 		# cursor3.execute('SELECT course_id,status FROM regiscourse')

# 		templates = {

# 			'course' : cursor.fetchall(),
# 			'enroll' : cursor2.fetchall(),
# 			# 'status' : cursor3.fetchall(),

# 			}

# 		template = JINJA_ENVIRONMENT.get_template('course.html')
# 		self.response.write(template.render(templates))


		
	

# class Toggle(webapp2.RequestHandler):
# 	def get(self):

# 		value=self.request.get('course_id');
# 		value=int(value)
		
				

# 		conn = rdbms.connect(instance=_INSTANCE_NAME, database='Prinya_Project')
#     		cursor = conn.cursor()
#     		sql1="SELECT status FROM regiscourse WHERE course_id= '%d'"%value
#     		cursor.execute(sql1);
#     		result=cursor.fetchall()

#     		for row in result:
# 			if row[0]==1:
# 				sql2="UPDATE regiscourse set status=0 where course_id='%d'"%value

# 				cursor.execute(sql2);
				

# 			else:
# 				sql3="UPDATE regiscourse set status=1 where course_id='%d'"%value
# 				cursor.execute(sql3);

				
# 			conn.commit()
# 			conn.close()
# 			self.redirect("/")

# class Notification(webapp2.RequestHandler):
# 	def get(self):

# 		conn = rdbms.connect(instance=_INSTANCE_NAME, database='Prinya_Project')
# 	    	cursor = conn.cursor()
# 	    	sql = ("""select log_id,course_name,day,time,l.type,l.staff_id,firstname,email 
# 					from log l join staff s 
# 					on l.staff_id=s.staff_id 
# 					join course c
# 					on c.course_id=l.course_id
# 					order by log_id desc""")
# 		cursor.execute(sql)

# 		templates = {

# 					'log' : cursor.fetchall(),
# 					}

# 		template = JINJA_ENVIRONMENT.get_template('notification.html')
# 		self.response.write(template.render(templates))
			
# 		conn.close();

class Search(webapp2.RequestHandler):
	def get(self):

		value = self.request.get('query');

		templates = {

					 'value' : value,
					}

		template = JINJA_ENVIRONMENT.get_template('index.html')
		self.response.write(template.render(templates))



app = webapp2.WSGIApplication([
    ('/', Search),	
], debug=True)
