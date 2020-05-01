# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:07:29 2020

@author: Ching
"""
import csv 
import itertools
import sys


#-------------------------------------------------------------------------------------------------
####Get and prepare data for processing####

#Initializes input and out file path 
try:
    input_path = sys.argv[1]
except:
    input_path = "../input/complaints.csv"
try:
    output_path = sys.argv[2]
except:
    output_path = "../output/report.csv"


#Read input file specified by input path
#Create a two dimensional list storing the data in input file
with open(input_path, 'r', newline='', encoding = 'utf-8') as csvfile:
    data_obj = csv.reader(csvfile, delimiter=',',quotechar='"')
    data = []
    for row in data_obj:
        data.append(row)
    data = data[1:]


#sort data according to accending order of time and alphabetic order of product name
data.sort(key=lambda x: (x[0], x[1]))


#Get lists of unique product, year, company
product = [i[1] for i in data]
product_unique = list(set(product))
year = [i[0].split('-')[0] for i in data]
year_unique = list(set(year))
year_unique.sort()
company = [i[7] for i in data]
company_unique = list(set(company))



#---------------------------------------------------------------------------------------------------
####Process data to create output####

#initialize report3 as an empty 2-d list for storing processed analytics
#each row represents 1 specific product x year pair 
report3 = []
for i in itertools.product(product_unique, year_unique):
    report3.append(i)

#Create data subsets grouped by product x year pair
#all data in the same group will have same product x year
dataSubset = []
for i in range(len(report3)):
    dataSubset.append([])

#allocate each data row/record to data subset with matching produc x year pair
for z in data:
    for i in range(len(report3)):
        if z[1]==report3[i][0] and z[0].split('-')[0]==report3[i][1]:
            dataSubset[i].append(z)

#Process data in data subset to obtain desired outputs
for i in range(len(report3)):          
    #initializes outputs and list to store company
    TotalComplaint = 0
    TotalNumCompanies = 0
    CompanyList = [] 
    #Initialize a dictionary to store number of complaints for individual companies
    #complaints are intialized as 0
    CompDict = {}    
    for m in range(len(company_unique)):
        CompDict[company_unique[m]] = 0 
    
    #Get total number of complaint of each product x pair/each data subset
    TotalComplaints = len(dataSubset[i])
    
    #get a comprehensive non-unique list of companies for each product x year pair/each data subset
    #count and store complaints for each company
    for ii in dataSubset[i]:
        CompanyList.append(ii[7])
        CompDict[ii[7]] = CompDict[ii[7]]+1
    #get a unique list of companies; count total number of companies in the list for each product x year pair
    TotalNumCompanies = len(list(set(CompanyList)))
    
    #sort company based on number of complaints 
    CompDict_S3 = sorted(CompDict.items(), key=lambda x: x[1], reverse=True)   
    #get top percentage of complaint out of all companies for product x year pair
    if TotalComplaints != 0:
        TopPercent = round(CompDict_S3[0][1]/TotalComplaints*100)
    else:
        TopPercent = 0
    
    #add total number of complaints, total number of companies, top percentage of complaint to report 
    report3[i] = report3[i] + (TotalComplaints,TotalNumCompanies,TopPercent)



#-------------------------------------------------------------------------------------------------------
#Format output data and write to csv file

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
    row[0] = row[0].lower()

#create a csv file in GitHub top most output directory; write output report to this csv
with open(output_path, 'w', newline='') as csvfile:
    output = csv.writer(csvfile, delimiter=',', quotechar='"')
    output.writerows(report_output)   









