# importing csv module
import csv
# csv file name
filename = "ind_nifty100list.csv" #list of nifty 100 stocks
filename2= "CMVOLT.CSV" #records for all the stocks with daily Volatility info
filename3 = "nifvol.csv" #output file with only nifty 100 stocks and their daily Volatility

# initializing the titles and rows list
fields = []#storing first row i.e. header for nifty 100 stocks i.e filename
rows = []#records for filename
fields2=[]#header list for filename2
rows2=[]#records for filename2

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
    
    # extracting field names through first row
    fields = csvreader.next()

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

    # get total number of rows
    print("Total no. of rows in file1: %d"%(csvreader.line_num))
    
    
#for file 2

with open(filename2, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
    
    # extracting field names through first row
    fields2 = csvreader.next()

    # extracting each data row one by one
    for row in csvreader:
        rows2.append(row)

    # get total number of rows
    print("Total no. of rows in file2: %d"%(csvreader.line_num))


# printing the field names
#print('Field names are:' + ', '.join(field for field in fields))
#print('Field2 names are:' + ', '.join(field for field in fields2))

#Reading and Writing to New File

# field names and row initializing for output.csv i.e filename3
fields3 = ['Symbol', 'Company Name', 'Today\'s Close Price', 'Yesterday\'s Close Price', 'Previous Day Volatility', 'Current Day Volatility', 'Annualised Volatility']
rows3 = []

#scanning each row of filename2 and then checking corresponding company name in filename1
for row2 in rows2:
    #print(row2[1]+'\n')
    for row in rows:
        if row[2] == row2[1]:
            temp = [row[2],row[0],row2[2],row2[3],(float(row2[5])*100),(float(row2[6])*100),(float(row2[7])*100)]
            rows3.append(temp)
 
# writing to csv file
with open(filename3, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
     
    # writing the fields
    csvwriter.writerow(fields3)
     
    # writing the data rows
    csvwriter.writerows(rows3)
