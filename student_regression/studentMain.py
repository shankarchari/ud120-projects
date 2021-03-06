# -*- coding: utf-8 -*-
# @Author: Gowri Shankar
# @Date:   2016-05-29 19:28:29
# @Last Modified by:   Gowri Shankar
# @Last Modified time: 2016-05-29 21:38:35

#!/usr/bin/python
import numpy 
import matplotlib
matplotlib.use('agg')

import matplotlib.pyplot as plt 
from studentRegression import studentReg 
from class_vis import prettyPicture, output_image

from ages_net_worths import ageNetWorthData

ages_train, ages_test, net_worths_train, net_worths_test = ageNetWorthData()


reg = studentReg(ages_train, net_worths_train)

print "Net worth prediction", reg.predict([27])
print "slope", reg.coef_
print "intercept", reg.intercept_

print "Stats on dataset"
print "r-squared score:", reg.score(ages_test, net_worths_test)

print "r-squared score:", reg.score(ages_train, net_worths_train)

plt.clf()
plt.scatter(ages_train, net_worths_train, color="b", labe="train data")
plt.scatter(ages_test, net_worths_test, color="r", label="test data")
plt.plot(ages_test, reg.predict(ages_test), color="black")
plt.legend(loc=2)
plt.xlabel("ages")
plt.ylabel("net worths")

plt.savefig("test.png")
output_image("test.png", "png", open("test.png", "rb").read())