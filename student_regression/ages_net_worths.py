# -*- coding: utf-8 -*-
# @Author: Gowri Shankar
# @Date:   2016-05-29 21:26:57
# @Last Modified by:   Gowri Shankar
# @Last Modified time: 2016-05-29 21:51:43


import numpy
import random

def ageNetWorthData():

	random.seed(42)
	numpy.random.seed(42)

	ages = [random.randint(20, 65) for ii in range(100)]

	net_worths = [ii * 6.25 + numpy.random.normal(scale=40.) for ii in ages]
	ages = numpy.reshape( numpy.array(ages), (len(ages), 1))
	net_worths = numpy.reshape( numpy.array(net_worths), (len(net_worths), 1))

	from sklearn.cross_validation import train_test_split
	ages_train, ages_test, net_worths_train, net_worths_test = train_test_split(ages, net_worths)

	return ages_train, ages_test, net_worths_train, net_worths_test