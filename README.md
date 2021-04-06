# Sales-Report
Sales Report for a grocery store in Python, full documentation and testing is included.
Part 1:
You are working on sorting data for a sales report in a grocery store. You are provided with a list of Transactions (sales for that day - see data definition in code). The function sales_report(transactions) consumes an unsorted list of distinct Transactions, and returns a new sorted list.

The output list contains the same data as the input list, but the data should be sorted by date, oldest to newest, and then by amount, from lowest to highest.

Part 2:
The second function top_sales(sorted_transactions) consumes a non-empty sorted list as given by the output of sales_report on a list of Transactions. This function prints a report showing the top sale for each unique day that appears in sorted_transactions, ordered from oldest to newest transaction.

The report has the following structure:
- Line 1: The title "Top Sales:"
- Line 2: The date range of the report. The format for this line is: "MMM DD, YYYY - MMM DD, YYYY", where MMM is a 3-letter code for month, taken from the list below, DD and YYYY correspond to the 2-digit Day and 4-digit Year from the date field in the top Transaction for that day.
- Line 3: Blank line
- Lines 4+: One line for each unique day in the report, detailing the highest sale of that day. The format for this line is "DD-MM-YYYY: $Amount SalesPerson". These fields are separated by a space only. The date is the same format as in a Transaction. The Amount is the top sale of that day, formatted with a leading dollar sign, and displayed to 2 decimals.

Month Codes:

![image](https://user-images.githubusercontent.com/67871488/113642316-8bfa0a80-964d-11eb-80f8-97e2a15cebd7.png)
