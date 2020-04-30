# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:07:29 2020

@author: Ching
"""
import csv 
import itertools
import urllib

#Read input data from local csv file
#with open(r"C:\Users\Ching\Documents\complaints.csv", 'r', newline='', encoding = 'utf-8') as csvfile:
#    data_obj = csv.reader(csvfile, delimiter=',',quotechar='"')
#    data = []
#    for row in data_obj:
#        data.append(row)
#    data = data[1:]

#Read input data from GitHub csv file 
data_file = urllib.request.urlopen("https://github.com/ChinghongWu/Insight_DataEngineering_CodeChallenge/tree/master/input/complaints.csv").read()
data_obj = csv.reader(data_file, delimiter=',',quotechar='"')
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




#Method 3
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






##Method 1
#report = []
#for i in itertools.product(product_unique, year_unique):
#    report.append(i)
#
##Get total number of complaints received for each product and each year
#n = 0
#for i,j in (report): 
#    report[n] = report[n] + (sum(1 for x in data if x[1]==i and x[0].split('-')[0]==j),)
#    n = n + 1
#
##Get the number of companies receiving the complaints for each product each year
#n = 0
#curListOfComp = [] 
#for i,j,k in (report):
#    numOfComp = 0
#    for y in data: 
#        if y[1]==i and y[0].split('-')[0]==j and y[7] not in curListOfComp:
#            curListOfComp.append(y[7])
#            numOfComp += 1
#    report[n] = report[n] + (numOfComp,)
#    n+=1
#    print(0)
#
#
##Get the highest percentage of complaints directed at a single comapny per product and per year
#n=0
#for i,j,k,l in (report):
#    CompDict = {}
#    for m in range(len(company_unique)):
#        CompDict[company_unique[m]] = 0 
#    for z in data:
#        if z[1]==i and z[0].split('-')[0]==j:   #this is not evaluated
#            CompDict[z[7]] = CompDict[z[7]]+1
#    CompDict_S = sorted(CompDict.items(), key=lambda x: x[1], reverse=True)      
#    report[n] = report[n] + (CompDict_S[0][1],)
#    n+=1
##Output file: list unique pairs of product and year 
##Each line includes: product, year, 
##                    total num of complaints, total num of companies receiving complaints 
##                    highest percentage of total complaints filed against one company 
##Sort lines in out file in ascending year and alphabatically by product








