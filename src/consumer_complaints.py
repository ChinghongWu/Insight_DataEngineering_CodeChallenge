# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:07:29 2020

@author: Ching
"""
import csv 
import itertools
import sys

#local path for testing
#input_path = "C:/Users/Ching/Documents/complaints.csv"
#output_path = "C:/Users/Ching/Documents/report.csv "

#Github directory path for testing 
try:
    input_path = sys.argv[1]
except:
    input_path = "../input/complaints.csv"

try:
    output_path = sys.argv[2]
except:
    output_path = "../output/report.csv"


with open(input_path, 'r', newline='', encoding = 'utf-8') as csvfile:
    data_obj = csv.reader(csvfile, delimiter=',',quotechar='"')
    data = []
    for row in data_obj:
        data.append(row)
    data = data[1:]

#sort data according to accending order of time and alphabetic order of product name
data.sort(key=lambda x: (x[0], x[1]))

#Get lists of unique product and unique years
product = [i[1] for i in data]
product_unique = list(set(product))
year = [i[0].split('-')[0] for i in data]
year_unique = list(set(year))
year_unique.sort()
company = [i[7] for i in data]
company_unique = list(set(company))



#Method 3s
report3 = []
dataSubset = []
CompanyList = []
n = 0

for i in itertools.product(product_unique, year_unique):
    report3.append(i)

for i in range(len(report3)):
    dataSubset.append([])

#subset data based on year product pair
for z in data:
    for i in range(len(report3)):
        if z[1]==report3[i][0] and z[0].split('-')[0]==report3[i][1]:
            dataSubset[i].append(z)

for i in range(len(report3)):        
    TotalComplaint = 0
    TotalNumCompanies = 0
    CompanyList = [] #company list (include repetitions) for product x year pair
    
    #all possible companies 
    CompDict = {}    
    for m in range(len(company_unique)):
        CompDict[company_unique[m]] = 0 
    
    #get total number of complaint of each subset (each set represent data for product x year pair)
    TotalComplaints = len(dataSubset[i])
    
    #get non-unique list of companies for product x year, and count complaints per company
    for ii in dataSubset[i]:
        CompanyList.append(ii[7])
        CompDict[ii[7]] = CompDict[ii[7]]+1
    
    #get the total number of company from unique list of company 
    TotalNumCompanies = len(list(set(CompanyList)))
    
    #sort company based on number of complaints 
    CompDict_S3 = sorted(CompDict.items(), key=lambda x: x[1], reverse=True)   
    
    #get top percentage of complaint out of all companies for product x year pair
    if TotalComplaints != 0:
        TopPercent = round(CompDict_S3[0][1]/TotalComplaints*100)
    else:
        TopPercent = 0
    
    #add all number to report 
    report3[i] = report3[i] + (TotalComplaints,TotalNumCompanies,TopPercent)

#delete rows in report if there is no complaints filed
j = 0
while j < len(report3):
    if report3[j][2] == 0:
        report3.remove(report3[j])
    else:
        j+=1       
        
#Structure report format to 2d list, sorted alphabetically and in ascending year
report_output = []
for row in report3:
    report_output.append(list(row))
report_output.sort(key=lambda x: (x[0], x[1])) 

#covert from year column from string to int
for row in report_output:
    row[1] = int(row[1])




#upload report as a csv file to GitHub top most output directory 
with open(output_path, 'w', newline='') as csvfile:
    output = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    output.writerows(report3)   









