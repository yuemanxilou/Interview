#! /usr/bin/python
# coding:utf-8
__author__ = 'Michael'
import requests

# r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
# print r.content
# # print r.headers
# # print r.text
# # print r.json()
# # print r.encoding

r = requests.post("http://httpbin.org/post")
print r.status_code

payload = {}