from unittest import TestCase
import requests
import json

class CheckRootSquareSolver(TestCase):
  url = 'http://localhost:5000/users'
  headers = { 'Content-Type': 'application/json' }
  id = None
  payload = {
    "name": "Harry Potter",
    "age": "2",
    "address": "JK Rowling"
  }
  
  def test_create(self):
    response = requests.post(self.url, headers=self.headers, data=json.dumps(self.payload))
    data = response.json()
    
    self.assertEqual(data['name'], self.payload['name'])
    self.assertEqual(data['age'], self.payload['age'])
    self.assertEqual(data['address'], self.payload['address'])
    
    self.id = str(data['id'])
    
    url = self.url + '/' + self.id
    payload = self.payload
    payload['age'] = '30'
    response = requests.put(url, headers=self.headers, data=json.dumps(payload))
    data = response.json()
    
    self.assertEqual(data['age'], self.payload['age'])
    
  def test_update(self):
    yield