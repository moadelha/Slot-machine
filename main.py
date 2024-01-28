import random

MAX_LINES = 3 #when do it in capital make it a constant 
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
            else:
                winnings += values[symbol] * bet
                winning_lines.append(line + 1)
    return winnings, winning_lines 


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count): # _ is an annonymous variable we ue if we don't care about the value 
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:] #add [:] to make a copy
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end="|")
            else:
                print(column[row], end="\n")


def deposit():
    
    while True:
        amount = input("Enter the amount you want to Deposite: ")
        
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else: 
                print("Enter a amount greater than 0")
        else: 
            print("Pleae enter a number ")
    
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the  number of line between (1-" + str(MAX_LINES) +"): ")
        
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else: 
                print("Enter a valid number of lines")
        else: 
            print("Pleae enter a number ")
    
    return lines

def get_bet():
    while True:
        amount = input("Enter the amount you want to Bet: ")
        
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else: 
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else: 
            print("Pleae enter a number ")
    
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if bet > balance:
            print(f"You dont have enough to bet your balance is ${balance}")
            increace = input("Would you like to make a deposite[y/n]? ")
            if increace == "y":
                added_amount = deposit()
                balance = balance + added_amount
            else:
                break
        else: 
            break
    
    print(f"You are betting ${bet} on {lines} your total bet is ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"you won {winnings}")
    print(f"you won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"current balance is  ${balance}")
        answer = input("Press enter to play or q to quit")
        if answer == "q":
            break
        balance += spin(balance)
main()