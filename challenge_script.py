import csv
import matplotlib.pyplot as pyplot
import numpy

# Lists to sort member_ids in to respective owner type
rent_member_id_list = []
mortgage_member_id_list = []
own_member_id_list = []
# Segregating owners into corresponding lists 
with open(file="home_ownership_data.csv", mode="r", encoding="utf-8") as csvfile:
    ownership_file = csv.reader(csvfile, delimiter=",")
    for row in ownership_file:
        if str(row[1]) == "RENT":
            rent_member_id_list.append(row[0])
        elif str(row[1]) == "MORTGAGE":
            mortgage_member_id_list.append(row[0])
        elif str(row[1]) == "OWN":
            own_member_id_list.append(row[0])

# Making dicionary to store just member_id and loan amount
loans_dict = dict()
with open(file="loan_data.csv", mode="r", encoding="utf-8") as csvfile:
    loan_file = csv.reader(csvfile, delimiter=",")
    ignore_loop = True
    for row in loan_file:
        if ignore_loop:
            ignore_loop = False
            continue

        loans_dict.setdefault(row[0], row[1]) 

rent_amount_list = []
mortgage_amount_list = []
own_amount_list = []
for member in rent_member_id_list:
    item = loans_dict.pop(member)
    rent_amount_list.append(int(item))
for member in mortgage_member_id_list:
    item = loans_dict.pop(member)
    mortgage_amount_list.append(int(item))
for member in own_member_id_list:
    item = loans_dict.pop(member)
    own_amount_list.append(int(item))

# Avg values for ownership loans 
avg_rent_loan = sum(rent_amount_list)/len(rent_amount_list)
avg_mortgage_loan = sum(mortgage_amount_list)/len(mortgage_amount_list)
avg_own_loan = sum(own_amount_list)/len(own_amount_list)

# print("Rent = " + str(avg_rent_loan))
# print("Mortgage = " + str(avg_mortgage_loan))
# print("Own = " + str(avg_own_loan))

# Making bar graph 
label = ["RENT", "MORTGAGE", "OWN"]
data = [avg_rent_loan, avg_mortgage_loan, avg_own_loan]

index = numpy.arange(len(label))
pyplot.bar(index, data)
pyplot.xlabel("Home Ownership", fontsize = 10)
pyplot.ylabel("Average loan amount ($)", fontsize=10)
pyplot.xticks(index, label, fontsize=10)
pyplot.title("Average loan amounts per ownership")
pyplot.show()









