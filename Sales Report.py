##
##=======================================================
## Jaskirat Pabla
## Sales Report
##=======================================================
##


import check


## Data Definition:

## A Transaction is a (list Str Float Str)
## Requires:
##    First String is a valid date of the transaction
##      in the format DD-MM-YYYY
##    Middle Float is the amount of the transaction 
##      to at most 2 decimal places
##    Last String represents the name of the sales person


## Global Constants:
line_one = "Top Sales:"
line_three = ''
lst_of_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


##########################  PART 1  ##########################


def sales_report(transactions):
    '''
    Returns a list that contains the same elements as transactions,
    however the list is sorted by date, oldest to newest, and
    then by amount, from lowest to highest.
    
    sales_report: (listof Transaction) -> (listof Transaction)
    Requires: Each Transaction in transactions is distinct.
    
    Examples:
        If L = [] then
        sales_report(L) => []
        
        If L = [['01-01-0001', 0.01, 'Adam']] then
        sales_report(L) => [['01-01-0001', 0.01, 'Adam']]
        
        If L = [['31-01-2021', 9999928.22 , 'Adam'], 
               ['02-02-2021', 71.52, 'Adam'], 
               ['01-02-2021', 120200.45, 'Oliver'], 
               ['02-02-2021', 85.66, 'Adam'], 
               ['31-01-2021', 47534.66, 'Celine'], 
               ['03-02-2021', 77.2, 'Frank'], 
               ['02-02-2021', 31.12, 'Celine'], 
               ['03-02-2021', 44.37, 'Celine']] then
        sales_report(L) => [['31-01-2021', 47534.66, 'Celine'], 
                            ['31-01-2021', 9999928.22, 'Adam'],
                            ['01-02-2021', 120200.45, 'Oliver'], 
                            ['02-02-2021', 31.12, 'Celine'], 
                            ['02-02-2021', 71.52, 'Adam'], 
                            ['02-02-2021', 85.66, 'Adam'], 
                            ['03-02-2021', 44.37, 'Celine'], 
                            ['03-02-2021', 77.2, 'Frank']]
    '''
    sort_by_amount = sorted(transactions, 
                            key = lambda transaction: transaction[1])
    sort_by_day = sorted(sort_by_amount,
                         key = lambda transaction: transaction[0][0:2])
    sort_by_month = sorted(sort_by_day,
                           key = lambda transaction: transaction[0][3:5])
    sort_by_year = sorted(sort_by_month,
                          key = lambda transaction: transaction[0][6:10])
    final_sorted_lst = sort_by_year
    return final_sorted_lst

## Examples:
L = []
check.expect('empty list', sales_report(L), [])

L = [['01-01-0001', 0.01, 'Adam']]
check.expect('list of only one Transaction', sales_report(L), 
             [['01-01-0001', 0.01, 'Adam']])

L = [['31-01-2021', 9999928.22 , 'Adam'], 
     ['02-02-2021', 71.52, 'Adam'], 
     ['01-02-2021', 120200.45, 'Oliver'], 
     ['02-02-2021', 85.66, 'Adam'], 
     ['31-01-2021', 47534.66, 'Celine'], 
     ['03-02-2021', 77.2, 'Frank'], 
     ['02-02-2021', 31.12, 'Celine'], 
     ['03-02-2021', 44.37, 'Celine']]
check.expect('Typical case', sales_report(L),
             [['31-01-2021', 47534.66, 'Celine'], 
              ['31-01-2021', 9999928.22, 'Adam'],
              ['01-02-2021', 120200.45, 'Oliver'], 
              ['02-02-2021', 31.12, 'Celine'], 
              ['02-02-2021', 71.52, 'Adam'], 
              ['02-02-2021', 85.66, 'Adam'], 
              ['03-02-2021', 44.37, 'Celine'], 
              ['03-02-2021', 77.2, 'Frank']])

## Tests:
L = [['31-01-2020', 9999928.22 , 'Adam'], 
     ['02-02-2019', 71.52, 'Adam'], 
     ['01-02-2020', 120200.45, 'Oliver'], 
     ['02-02-2020', 85.66, 'Adam'], 
     ['31-01-2021', 47534.66, 'Celine'], 
     ['03-02-2021', 77.2, 'Frank'], 
     ['02-02-2019', 31.12, 'Celine'], 
     ['03-02-2021', 44.37, 'Celine']]
check.expect('transactions from different years', sales_report(L),
             [['02-02-2019', 31.12, 'Celine'],
              ['02-02-2019', 71.52, 'Adam'],
              ['31-01-2020', 9999928.22 , 'Adam'],
              ['01-02-2020', 120200.45, 'Oliver'],
              ['02-02-2020', 85.66, 'Adam'],
              ['31-01-2021', 47534.66, 'Celine'],
              ['03-02-2021', 44.37, 'Celine'],
              ['03-02-2021', 77.2, 'Frank']])

L = [['25-06-2000', 9999928.22 , 'Adam'], 
     ['25-06-2000', 71.52, 'Adam'], 
     ['25-06-2000', 120200.45, 'Oliver'], 
     ['25-06-2000', 85.66, 'Adam'], 
     ['25-06-2000', 47534.66, 'Celine'], 
     ['25-06-2000', 77.2, 'Frank'], 
     ['25-06-2000', 31.12, 'Celine'], 
     ['25-06-2000', 44.37, 'Celine']]
check.expect('transactions on the same day', sales_report(L),
             [['25-06-2000', 31.12, 'Celine'],
              ['25-06-2000', 44.37, 'Celine'],
              ['25-06-2000', 71.52, 'Adam'],
              ['25-06-2000', 77.2, 'Frank'],
              ['25-06-2000', 85.66, 'Adam'],
              ['25-06-2000', 47534.66, 'Celine'],
              ['25-06-2000', 120200.45, 'Oliver'],
              ['25-06-2000', 9999928.22 , 'Adam']])

L = [['25-06-1995', 100.1, 'Adam'], 
     ['25-06-2025', 100.1, 'Adam'], 
     ['25-06-1057', 100.1, 'Oliver'], 
     ['25-06-0049', 100.1, 'Adam'], 
     ['25-06-9999', 100.1, 'Celine'], 
     ['25-06-1996', 100.1, 'Frank'], 
     ['25-06-1995', 100.1, 'Celine'], 
     ['25-06-2025', 100.1, 'Celine']]
check.expect('transactions with the same amount', sales_report(L),
             [['25-06-0049', 100.1, 'Adam'],
              ['25-06-1057', 100.1, 'Oliver'],
              ['25-06-1995', 100.1, 'Adam'],
              ['25-06-1995', 100.1, 'Celine'],
              ['25-06-1996', 100.1, 'Frank'],
              ['25-06-2025', 100.1, 'Adam'], 
              ['25-06-2025', 100.1, 'Celine'],
              ['25-06-9999', 100.1, 'Celine']])


##########################  PART 2  ##########################


def highest_sale_of_each_day_printer(transaction_lst):
    '''
    Prints the top sale for each unique day that appears in 
    transaction_lst on a seperate line, ordered from oldest 
    to newest.
    
    Effects: Prints to the screen.
    
    highest_sale_of_each_day_printer: (listof Transaction) -> None
    Requires: transaction_lst must be a non-empty sorted list as
    given by the output of sales_report on a list of Transaction.
    '''
    lst_of_unique_dates = []
    lst_of_highest_sales = []
    rev_transactions = transaction_lst.copy()
    rev_transactions.reverse()
    for transaction in rev_transactions:
        if transaction[0] not in lst_of_unique_dates:
            lst_of_highest_sales.append(transaction)
            lst_of_unique_dates.append(transaction[0])
    lst_of_highest_sales.reverse()
    for sale in lst_of_highest_sales:
        sale_date = sale[0]
        sale_price = sale[1]
        sale_representative = sale[2]
        print_line = '{0}: ${1:.2f} {2}'.format(sale_date, sale_price,
                                                sale_representative)
        print(print_line)


def top_sales(sorted_transactions):
    '''
    Prints a report showing the top sale for each unique day that
    appears in sorted_transactions, ordered from oldest to newest.
  
    Effects: Prints to the screen.
  
    top_sales: (listof Transaction) -> None
    Requires: sorted_transactions must be a non-empty sorted list
    as given by the output of sales_report on a list of Transaction.
    
    Examples:
        If L = [['01-01-0001', 0.01, 'Adam']] then
        top_sales(L) => None and the following is printed:
            Top Sales:
            Jan 01, 0001 - Jan 01, 0001
  
            01-01-0001: $0.01 Adam
        
        If L = [['31-01-2021', 47534.66, 'Celine'], 
                ['31-01-2021', 9999928.22, 'Adam'], 
                ['01-02-2021', 120200.45, 'Oliver'], 
                ['02-02-2021', 31.12, 'Celine'], 
                ['02-02-2021', 71.52, 'Adam'], 
                ['02-02-2021', 85.66, 'Adam'], 
                ['03-02-2021', 44.37, 'Celine'], 
                ['03-02-2021', 77.20, 'Frank']] then
        top_sales(L) => None and the following is printed:
            Top Sales: 
            Jan 31, 2021 - Feb 03, 2021
  
            31-01-2021: $9999928.22 Adam
            01-02-2021: $120200.45 Oliver
            02-02-2021: $85.66 Adam
            03-02-2021: $77.20 Frank
    '''
    print(line_one)
    
    start_date = sorted_transactions[0][0]
    end_date = sorted_transactions[-1][0]
    
    start_day = start_date[0:2]
    end_day = end_date[0:2]
    
    start_month_index = int(start_date[3:5])-1
    end_month_index = int(end_date[3:5])-1
    start_month = lst_of_months[start_month_index]
    end_month = lst_of_months[end_month_index]
    
    start_year = start_date[6:10]
    end_year = end_date[6:10]
    
    line_two = '{0} {1}, {2} - {3} {4}, {5}'.format(start_month, start_day,
                                                  start_year, end_month,
                                                  end_day, end_year)
    print(line_two)
    print(line_three)
    highest_sale_of_each_day_printer(sorted_transactions)


## Examples:
L = [['01-01-0001', 0.01, 'Adam']]
check.set_print_exact(line_one, 'Jan 01, 0001 - Jan 01, 0001',
                      line_three, '01-01-0001: $0.01 Adam')
check.expect('list of only one sale', top_sales(L), None)

L = [['31-01-2021', 47534.66, 'Celine'], 
     ['31-01-2021', 9999928.22, 'Adam'], 
     ['01-02-2021', 120200.45, 'Oliver'], 
     ['02-02-2021', 31.12, 'Celine'], 
     ['02-02-2021', 71.52, 'Adam'], 
     ['02-02-2021', 85.66, 'Adam'], 
     ['03-02-2021', 44.37, 'Celine'], 
     ['03-02-2021', 77.20, 'Frank']]
check.set_print_exact(line_one, 'Jan 31, 2021 - Feb 03, 2021',
                      line_three, '31-01-2021: $9999928.22 Adam\n'
                      '01-02-2021: $120200.45 Oliver\n'
                      '02-02-2021: $85.66 Adam\n'
                      '03-02-2021: $77.20 Frank')
check.expect('Typical case', top_sales(L), None)


## Tests:
L = [['02-02-2019', 31.12, 'Celine'],
     ['02-02-2019', 71.52, 'Adam'],
     ['31-01-2020', 9999928.22 , 'Adam'],
     ['01-02-2020', 120200.45, 'Oliver'],
     ['02-02-2020', 85.66, 'Adam'],
     ['31-01-2021', 47534.66, 'Celine'],
     ['03-02-2021', 44.37, 'Celine'],
     ['03-02-2021', 77.2, 'Frank']]
check.set_print_exact(line_one, 'Feb 02, 2019 - Feb 03, 2021',
                      line_three, '02-02-2019: $71.52 Adam\n'
                      '31-01-2020: $9999928.22 Adam\n'
                      '01-02-2020: $120200.45 Oliver\n'
                      '02-02-2020: $85.66 Adam\n'
                      '31-01-2021: $47534.66 Celine\n'
                      '03-02-2021: $77.20 Frank')
check.expect('transactions from different years', top_sales(L), None)

L = [['25-06-2000', 31.12, 'Celine'],
     ['25-06-2000', 44.37, 'Celine'],
     ['25-06-2000', 71.52, 'Adam'],
     ['25-06-2000', 77.2, 'Frank'],
     ['25-06-2000', 85.66, 'Adam'],
     ['25-06-2000', 47534.66, 'Celine'],
     ['25-06-2000', 120200.45, 'Oliver'],
     ['25-06-2000', 9999928.22 , 'Adam']]
check.set_print_exact(line_one, 'Jun 25, 2000 - Jun 25, 2000',
                      line_three, '25-06-2000: $9999928.22 Adam')
check.expect('transactions on the same day', top_sales(L), None)

L = [['25-06-0049', 100.1, 'Adam'],
     ['25-06-1057', 100.1, 'Oliver'],
     ['25-06-1995', 100.1, 'Adam'],
     ['25-06-1995', 100.1, 'Celine'],
     ['25-06-1996', 100.1, 'Frank'],
     ['25-06-2025', 100.1, 'Adam'], 
     ['25-06-2025', 100.1, 'Celine'],
     ['25-06-9999', 100.1, 'Celine']]
check.set_print_exact(line_one, 'Jun 25, 0049 - Jun 25, 9999',
                      line_three, '25-06-0049: $100.10 Adam\n'
                      '25-06-1057: $100.10 Oliver\n'
                      '25-06-1995: $100.10 Celine\n'
                      '25-06-1996: $100.10 Frank\n'
                      '25-06-2025: $100.10 Celine\n'
                      '25-06-9999: $100.10 Celine')
check.expect('transactions with the same amount', top_sales(L), None)
