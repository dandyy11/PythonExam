# Read the file VendorList.csv into this program and create a dictionary of the customer's
# full name, email address and phone number where the key is the full name of the customer
# and the value is a dictionary where the keys are 'email' and 'phone' and the values
# are the corresponding email address and phone number of the customer. So it is a dictionary
# within a dictionary. 

# Once the dictionary has been completed print it out. It shoud resemble what is shown
# below (first 2 and last 2 elements shown only):

#{'Tommie Goody': {'email': 'tgoody0@weather.com', 'phone': '809-992-7298'}, 
# 'Obadiah Godfery': {'email': 'ogodfery1@a8.net', 'phone': '560-745-9361'}......
# ..........'Kessiah Tynemouth': {'email': 'ktynemouthdu@ning.com', 'phone': '690-215-8097'}, 
# 'Carmela Kaubisch': {'email': 'ckaubischdv@wikia.com', 'phone': '307-726-6526'}}


# Using the dictionary, write the contents to a csv file. The output file shoud be exactly as
# what is shown in the file - marketinglist.csv.
# Name your file - marketinglistFINAL.csv


# Note: you can use the comments below to guide you through the logic of the code. You are not
# required to follow it. ALSO NOT ALL STEPS HAVE BEEN COMMENTED. You may have additional steps.

import csv

# open the vendorlist file
with open('VendorList.csv', mode='r') as infile:

    # create a csv object from the file object
    reader = csv.reader(infile)
    next(reader)  # Skip the header row

    # create an output file
    with open('marketinglistFINAL.csv', mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        
        # Write the header (optional, depending on if you need headers)
        # writer.writerow(['ID', 'First Name', 'Last Name', 'Email', 'Phone'])
        
        # iterate through the csv object and write the rows to the new file
        for row in reader:
            # Extract relevant fields: id, first_name, last_name, email, phone
            id = row[0]           # Assuming the first column is ID
            first_name = row[1]    # Assuming the second column is First Name
            last_name = row[2]     # Assuming the third column is Last Name
            email = row[4]         # Assuming the fifth column is Email
            phone = row[5]         # Assuming the sixth column is Phone
            
            # Write the row with required fields (excluding gender)
            writer.writerow([id, first_name, last_name, email, phone])


