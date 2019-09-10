import csv
import matplotlib.pyplot as pyplot
import numpy

# method to classify owners into corresponding lists 
def classify_owner(owner_type):
    """Method forms a collection of the specified owner type and returns a list of the owner member-ids"""
    owner_list = []
    with open(file="home_ownership_data.csv", mode="r", encoding="utf-8") as csvfile:
        ownership_file = csv.reader(csvfile, delimiter=",")
        for row in ownership_file:
            if str(row[1]) == owner_type:
                owner_list.append(row[0])
    return owner_list


def getMemberAndLoanData():
    """Method returns a dictionary with key: member_id and value: loan_amount"""
    loans_dict = dict()
    with open(file="loan_data.csv", mode="r", encoding="utf-8") as csvfile:
        loan_file = csv.reader(csvfile, delimiter=",")
        ignore_loop = True  # To ignore loop with header titles of csv file
        for row in loan_file:
            if ignore_loop:
                ignore_loop = False
                continue
            #Add data to a dictionary
            loans_dict.setdefault(row[0], row[1])
    return loans_dict

def get_loan_avg(member_id_list, data_dict):
    """Method computes and returns the average of loan amount values in provided list"""
    amount_list = []
    for member in member_id_list:
        item = data_dict.pop(member)
        amount_list.append(int(item))
    return sum(amount_list)/len(amount_list)


# Main method that produces data output
def generate_statistics():
    """Method calculates average loan amount for each ownership type and displays data as a graph"""

    rent_member_id_list = classify_owner("RENT")
    mortgage_member_id_list = classify_owner("MORTGAGE")
    own_member_id_list = classify_owner("OWN")

    loan_data_dict = getMemberAndLoanData()
    # # Avg values for ownership loans
    avg_rent_loan = get_loan_avg(rent_member_id_list, loan_data_dict)
    avg_mortgage_loan = get_loan_avg(mortgage_member_id_list, loan_data_dict)
    avg_own_loan = get_loan_avg(own_member_id_list, loan_data_dict)

    # Making bar graph 
    label = ["MORTGAGE", "OWN", "RENT"] # x-axis labels
    data = [avg_mortgage_loan,avg_own_loan, avg_rent_loan]
    index = numpy.arange(len(label))
    pyplot.bar(index, data)
    pyplot.xlabel("Home Ownership", fontsize = 10)
    pyplot.ylabel("Average loan amount ($)", fontsize=10)
    pyplot.xticks(index, label, fontsize=10)
    pyplot.title("Average loan amounts per home ownership")

    # Making table 
    fig = pyplot.figure()
    axis = fig.add_subplot(1,1,1)
    table_data = [
        ["MORTGAGE", format(avg_mortgage_loan, ".6f")], 
        ["OWN", format(avg_own_loan, ".6f")], 
        ["RENT", format(avg_rent_loan, ".6f")]
    ]
    table_headers = ["home_ownership", "loan_amnt"]
    table = pyplot.table(cellText=table_data, loc="center", colLabels = table_headers, cellLoc="center")
    table.set_fontsize(12)
    table.scale(1, 2)
    axis.axis("off")

    # Displaying data table and graph 
    pyplot.show()

if __name__ == "__main__":
    generate_statistics()









