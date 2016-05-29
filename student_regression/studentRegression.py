# -*- coding: utf-8 -*-
# @Author: Gowri Shankar
# @Date:   2016-05-29 19:28:29
# @Last Modified by:   Gowri Shankar
# @Last Modified time: 2016-05-29 21:11:23
def studentReg(ages_train, net_worths_train):
	from sklearn import linear_model
	req = linear_model.LinearRegression()
	reg.fit(ages_train, net_worths_train)


	return reg