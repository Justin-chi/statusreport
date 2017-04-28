import sys
sys.path.append('..')
from config import *
import requests
import simplejson as json

"""
  Project API
"""
def project_index(token):
  return requests.get(API_SERVER + '/api/projects', headers={'token':token})

"""
  Report API
"""
def report_index(token, week_filter, user_filter):
  user_param = '' if not user_filter else '?user='+user_filter
  return requests.get(API_SERVER + '/api/reports/' + week_filter + user_param, headers={'token':token})

def report_delete(token, id):
  return requests.delete(API_SERVER + '/api/reports/id/' + id, headers={'token':token})

def report_upsert(token, id, data):
  if id:
    data['report_id'] = id
    return requests.put(API_SERVER + '/api/reports/id/' + id, data=json.dumps(data), headers={'token':token})
  else:
    return requests.post(API_SERVER + '/api/reports', data=json.dumps(data), headers={'token': token})

