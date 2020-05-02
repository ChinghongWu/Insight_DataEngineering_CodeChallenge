# Insight_DataEngineering_CodeChallenge
This repo is dedicated to the Insight Fellowship program, focusing on development,testing for the code challenge

# Table of Contents
1. [Problem](README.md#Problem)
2. [Input](README.md#Input)
3. [Output](README.md#Output)
4. [Approach](README.md#Approach)
5. [Run Instruction](README.md#Run-Instruction)
6. [Tests](README.md#Tests)
7. [Contact](README.md#Contact)

# Problem
The federal government provides a way for consumers to file complaints against companies regarding different financial products, such as payment problems with a credit card or debt collection tactics. This challenge will be about identifying the number of complaints filed and how they're spread across different companies.

**For this challenge, we want to know for each financial product and year, the total number of complaints, number of companies receiving a complaint, and the highest percentage of complaints directed at a single company.

# Input
The python program takes comma separated CSV file as input
  * The input file has to be named complaints.csv and stored in the top-most directory of the repository
  * The input path is included in command line 

The input file containing a modest dataset of complaints can be found [Here](http://files.consumerfinance.gov/ccdb/complaints.csv.zip).

Due to the size of the dataset provided in the link, a portion of tests was conducted locally using the entire dataset.

Below are the contents of an example `complaints.csv` file: 
```
Date received,Product,Sub-product,Issue,Sub-issue,Consumer complaint narrative,Company public response,Company,State,ZIP code,Tags,Consumer consent provided?,Submitted via,Date sent to company,Company response to consumer,Timely response?,Consumer disputed?,Complaint ID
2019-09-24,Debt collection,I do not know,Attempts to collect debt not owed,Debt is not yours,"transworld systems inc. is trying to collect a debt that is not mine, not owed and is inaccurate.",,TRANSWORLD SYSTEMS INC,FL,335XX,,Consent provided,Web,2019-09-24,Closed with explanation,Yes,N/A,3384392
2019-09-19,"Credit reporting, credit repair services, or other personal consumer reports",Credit reporting,Incorrect information on your report,Information belongs to someone else,,Company has responded to the consumer and the CFPB and chooses not to provide a public response,Experian Information Solutions Inc.,PA,15206,,Consent not provided,Web,2019-09-20,Closed with non-monetary relief,Yes,N/A,3379500
2020-01-06,"Credit reporting, credit repair services, or other personal consumer reports",Credit reporting,Incorrect information on your report,Information belongs to someone else,,,Experian Information Solutions Inc.,CA,92532,,N/A,Email,2020-01-06,In progress,Yes,N/A,3486776
2019-10-24,"Credit reporting, credit repair services, or other personal consumer reports",Credit reporting,Incorrect information on your report,Information belongs to someone else,,Company has responded to the consumer and the CFPB and chooses not to provide a public response,"TRANSUNION INTERMEDIATE HOLDINGS, INC.",CA,925XX,,Other,Web,2019-10-24,Closed with explanation,Yes,N/A,3416481
2019-11-20,"Credit reporting, credit repair services, or other personal consumer reports",Credit reporting,Incorrect information on your report,Account information incorrect,I would like the credit bureau to correct my XXXX XXXX XXXX XXXX balance. My correct balance is XXXX,Company has responded to the consumer and the CFPB and chooses not to provide a public response,"TRANSUNION INTERMEDIATE HOLDINGS, INC.",TX,77004,,Consent provided,Web,2019-11-20,Closed with explanation,Yes,N/A,3444592
```

# Output
The python program output comma separated CSV file as output
* The output file is named report.csv and stored in the top-most output directory of the repository
* There are as many lines as unique pairs of product and year (of `Date received`) in the input file. 


Each line in the output file should list the following fields in the following order:
* product (name should be written in all lowercase)
* year
* total number of complaints received for that product and year
* total number of companies receiving at least one complaint for that product and year
* highest percentage (rounded to the nearest whole number) of total complaints filed against one company for that product and year. Use standard rounding conventions (i.e., Any percentage between 0.5% and 1%, inclusive, should round to 1% and anything less than 0.5% should round to 0%)

The lines in the output file should be sorted by product (alphabetically) and year (ascending)

Given the above `complaints.csv` input file, we'd expect an output file, `report.csv`, in the following format
```
"credit reporting, credit repair services, or other personal consumer reports",2019,3,2,67
"credit reporting, credit repair services, or other personal consumer reports",2020,1,1,100
debt collection,2019,1,1,100
```
# Approach:
The approach I used for processing the compliants data is:
* Parse all data into data subsets grouped by product-year pair, so that each subset contains data records of 1 specific product and year
* Count number of compliants of 1 specific product and year by counting the length of data subset
* Count total number of companies of 1 specific product and year by counting the length of unique list of companies in subset
* Count top percentage of complaints of 1 specific product and year by counting complaints for each companies in subset, dividing by total complaints, and sorting by percentage of complaints

# Run Instruction:
For this project, Python3.7 is used for solving the problem 

The **sys** library is used for accessing command line arguments in the python script. The command line arguements contain input path and output path.

Running the **run.sh** file in project root directory will execute the python script, and produce result in the top-most output directory of repository with the format specified by the challenge.

# Test:
Tests were manually run by placing complaints.csv found in the top-most directory.

A portion of tests were run using the entire dataset provided in [Here](http://files.consumerfinance.gov/ccdb/complaints.csv.zip.). These tests were carried out in local due to the upload size limit of GitHub. The local test provided useful insight regarding the processing speed of different methods used to solved the problem.

# Contact:
Feel free to contact [me](https://www.linkedin.com/in/chinghongwu/) 

## Shell Script: run.sh 
The run.sh file store in top level of repo is the shell script for executing consumer_complaints.py file. 
It passes two parameters to python file: input path, output path 

## Source code: consumer_complaints.py
The consumer_complaints.py file stored in ./src is the main source code for processing input file and output report


