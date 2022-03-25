#User can pick 6 number
import random
def menu():
    # perguntar os numeros
    user_numbers = get_player_number()
    # calcular loterry numbers
    loterry_numbers = create_lottery_numbers()
    # Print out the winnings
    matched_numbers = user_numbers.intersection(loterry_numbers)
    print("You matched {}. won ${}".format(matched_numbers,100 ** len(matched_numbers)))
def get_player_number():
    number_csv = input("Enter your 6 numbers, separate by commas: ")
    #Transform number string in integer
    number_list = number_csv.split(",")  # ['1','2','3','4']
    integer_set = {int(nine) for nine in number_list}
    return integer_set
#Lottery calculates 6 random number (betwn 1 and 20)
def create_lottery_numbers():
    values = set() # Cannot initialize like so: {}
    while len(values) < 6 :   # range in [0,1,2,3,4,5]
        values.add(random.randint(1,20))
    return values
menu()
print(get_player_number())
