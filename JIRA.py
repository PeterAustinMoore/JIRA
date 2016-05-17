import requests
import yaml
import json

base = 'https://socrata.atlassian.net'
with open('/Users/socrataintern/.soda.yml','r') as stream:
	config = yaml.load(stream)

open_issues_resource = '/rest/api/2/search?jql=status=open&maxResults=100000' 
closed_issues_resource = '/rest/api/2/search?jql=status=closed&maxResults=100000'
fields_resource = '/rest/api/2/field'

class JIRA(object):
	def __init__(self, username=None, password=None):
		self.username = username
		self.password = password
		
	def get_fields(self):
		resource = base + fields_resource

		response = requests.get(resource, auth=(self.username, self.password))
		if response != 200:
			return response.text

		data = json.loads(response.text)
		return data


	def get_open_issues(self):
		resource = base + open_issues_resource

		response = requests.get(resource, auth=(self.username,self.password))
		if response != 200:
			return response.text

		data = json.loads(response.text)
		return data

	def get_closed_issues(self):
		resource = base + closed_issues_resource

		response = requests.get(resource, auth=(self.username,self.password))
		if response != 200:
			return "closed issue error"

		data = json.loads(response.text)
		return data
	
	def map_fields(self, tickets):
		

	def get_data(self):
		all_tickets = []
		all_tickets.extend(self.get_open_issues())
		all_tickets.extend(self.get_closed_issues())

		cleaned_tickets = self.map_fields(all_tickets)
		
		return cleaned_tickets




jira = JIRA(username='peter.moore', password=config['jira_password'])
data = jira.get_fields()
print(data)