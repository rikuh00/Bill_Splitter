#%% GETS INPUTS
def get_num_ppl(): # Number of People Splitting the Bill
    ERROR_MSG = 'Invalid input - please try again'
    while True:
        try:
            num_ppl = int(input('Please enter the number of people splitting the bill: '))
        except ValueError:
            print(ERROR_MSG)
            continue
        else:
            if num_ppl == 0:
                print(ERROR_MSG)
                continue
            return num_ppl

def get_total_cost(): # Total Cost
    while True:
        try:
            total_cost = float(input('Please enter the total cost of the bill: $'))
        except ValueError:
            print('Invalid input - please try again.')
            continue
        else:
            return total_cost

def get_card(): # Gets if the Party is Paying by Cash/Credit - Determines Rounding
    while True:
        is_card = input('Is everyone paying by credit/debit card? ([Y]es or [N]o)').lower()
        if is_card == 'y':
            return True
        if is_card == 'n':
            return False
        continue

#%% CALCULATION & OUTPUT
def get_indiv_cost(num_ppl, total_cost, is_card): # Returns Cost Per Person + Additional Cost
    multiplier = 20.0 if is_card else 100.0
    indiv_cost = int((total_cost / num_ppl) * multiplier) / multiplier #lowest cost
    remaining_cost = total_cost - (indiv_cost * num_ppl)
    return indiv_cost, remaining_cost

def print_cost(num_ppl, total_cost, indiv_cost, remaining_cost): # Prints Cost Information
    print('\n')
    print('You have splitted a bill of ${:.2f} among {} people.'.format(total_cost, num_ppl))
    print('Each person has to pay ${:.2f}.'.format(indiv_cost))
    if remaining_cost != 0:
        print('In addition, one person has to pay an extra ${:.2f} to fully pay the bill.'.format(remaining_cost))
        print('This person will have to pay a total of ${:.2f}.'.format(indiv_cost + remaining_cost))

#%% MAIN
if __name__ == '__main__':
    num_ppl = get_num_ppl()
    total_cost = get_total_cost()
    is_card = get_card()
    indiv_cost, remaining_cost = get_indiv_cost(num_ppl, total_cost, is_card)
    print_cost(num_ppl, total_cost, indiv_cost, remaining_cost)