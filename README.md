# Insight_DataEngineering_CodeChallenge
This repo is dedicated to the Insight Fellowship program, focusing on development,testing for the code challenge

## Shell Script: run.sh 
The run.sh file store in top level of repo is the shell script for executing consumer_complaints.py file. 
It passes two parameters to python file: input path, output path 

## Source code: consumer_complaints.py
The consumer_complaints.py file stored in ./src is the main source code for processing input file and output report

## Approach:
The approach I used for processing the compliants data is:
* Parse all data into data subsets grouped by product-year pair, so that each subset contains data records of 1 specific product and year
* Count number of compliants of 1 specific product and year by counting the length of data subset
* Count total number of companies of 1 specific product and year by counting the length of unique list of companies in subset
* Count top percentage of complaints of 1 specific product and year by counting complaints for each companies in subset, dividing by total complaints, and sorting by percentage of complaints

