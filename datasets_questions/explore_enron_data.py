#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#print {k:v["total_stock_value"] for k, v in enron_data.iteritems()}
#print enron_data["PRENTICE JAMES"]["total_stock_value"]
print sum([1 for k, v in enron_data.iteritems() if v['salary'] != 'NaN'])
print sum([1 for k, v in enron_data.iteritems() if v['email_address'] != 'NaN'])
print sum([1 for k, v in enron_data.iteritems() if (v['total_payments'] == 'NaN' and v['poi'] == True) ])
print sum([1 for k, v in enron_data.iteritems() if v['poi'] == True ])