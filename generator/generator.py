import random


def generated_customer():
    customers = ["Hermoine Granger", "Harry Potter", "Ron Weasly", "Albus Dumbledore", "Neville Longbottom"]
    return customers[random.randrange(len(customers))]
