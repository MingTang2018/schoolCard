# -*- encoding:utf-8 -*-
import urllib2
import string
import re
import os
from sgmllib import SGMLParser 

class ListName(SGMLParser):
	"""docstring for ListName"""
	def __init__(self, arg):
		super(ListName, self).__init__()
		self.urls = []
		provincename =[]
		schoolname = []

	def start_a(self, attrs):
		for k, v in attrs:
			if k == 'class' and v == 'a13':