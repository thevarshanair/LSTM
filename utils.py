# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 13:48:28 2018

@author: VarshaNair
"""

import datetime as dt

class Timer():

	def __init__(self):
		self.start_dt = None

	def start(self):
		self.start_dt = dt.datetime.now()

	def stop(self):
		end_dt = dt.datetime.now()
		print('Time taken: %s' % (end_dt - self.start_dt))