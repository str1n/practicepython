# https://www.practicepython.org/

import datetime
import random


def exercise1():
    year = datetime.datetime.now().year
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    repeat = int(input("How many messages would you like? "))
    answer = year + (100 - age)

    while repeat > 0:
        print(f"Hi {name}, you will reach the age of 100 in the year {answer}")
        repeat = repeat - 1


def exercise2a():
    x = int(input("Input an integer: "))
    if (x % 4) == 0:
        print(f"{x} is divisible by 4")
    elif (x % 2) == 0:
        print(f"{x} is even.")
    else:
        print(f"{x} is odd.")


def exercise2b():
    num = int(input("Enter numerator: "))
    check = int(input("Enter divisor: "))
    if (num % check) == 0:
        print(f"{num}/{check} gives a remainder of zero.")
    else:
        print(f"{num} does not divide evenly by {check}.")


def exercise3():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    my_list = []
    cutoff = int(input("Enter number to filter list: "))
    for i in a:
        if i < cutoff:
            my_list.append(i)
    print(my_list)


def exercise4():
    x = int(input("Enter a number: "))
    nums = range(1, x)
    answer = []
    for i in nums:
        if (x % i) == 0:
            answer.append(i)
    print(f"The divisors of {x} are: {answer}")


def exercise5():
    start = int(input("Range start: "))
    end = int(input("Range end: "))
    a_len = int(input("First list length: "))
    b_len = int(input("Second list length: "))
    a_list = []
    b_list = []
    answer_list = []
    while a_len > 0:
        a_list.append(random.randint(start, end))
        a_len = a_len-1
    while b_len > 0:
        b_list.append(random.randint(start, end))
        b_len = b_len - 1
    print(f"List 1: {a_list}")
    print(f"List 2: {b_list}")
    for i in a_list:
        if i in b_list:
            if i not in answer_list:    # remove duplicates
                answer_list.append(i)
    print(f"Common elements: {answer_list}")


def exercise6():
    check = str(input("Enter a string and I will tell you if it is a palindrome: "))
    my_list = []
    for c in check:
        my_list.append(c)                       # convert string to list
    length = len(check)
    midpoint = length // 2                      # if odd length, can ignore middle char
    if (length % 2) == 0:                       # if odd length, need to drop middle char from second list to compare
        drop = 0                                # even so nothing to drop
    else:
        drop = 1                                # odd so must drop middle char
    a_list = my_list[0:midpoint]                # first half of list
    b_list = my_list[(midpoint+drop):length]    # second half of list to compare
    b_list.reverse()
    if a_list == b_list:
        print("It's a palindrome!")
    else:
        print("No joy!")


def exercise7():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    evens = [x for x in a if (x % 2) == 0]
    print(f"The even numbers are: {evens}")


def exercise8():
    player1 = str(input("Player1, Enter [R]ock / [P]aper / [S]cissors : "))
    player2 = str(input("Player2, Enter [R]ock / [P]aper / [S]cissors : "))
    order = ['R', 'P', 'S']
    score1 = 0
    score2 = 0
    for x in order:
        if player1.upper() == x:
            score1 = order.index(x)
        if player2.upper() == x:
            score2 = order.index(x)
    diff = score1 - score2
    result_lookup = {
        -2: "Player 1 wins",
        -1: "Player 2 wins",
        0: "It's a draw",
        1: "Player 1 wins",
        2: "Player 2 wins"
    }
    print(result_lookup[diff])


def exercise9():
    match = 0
    count = 0
    finish = 0
    target = random.randint(1, 9)
    while match == 0 and finish == 0:
        guess1 = input("Guess a number 1-9 inclusive: ")
        if guess1 == "exit":
            print("Bye!")
            finish = 1
        else:
            guess2 = int(guess1)
            count += 1
            if guess2 == target:
                match = 1
                print(f"You got it in {count} guesses")
            else:
                if target > guess2:
                    print("Too low")
                else:
                    print("Too high")


if __name__ == '__main__':
    print("Exercises: ")
    print("1. What year will be 100?")
    print("2a. Odd or even, or a multiple of 4?")
    print("2b. Zero remainder?")
    print("3. Lists part 1")
    print("4. Divisors of a number")
    print("5. Compare randomly generated lists")
    print("6. Palindromic lists")
    print("7. List comprehension")
    print("8. Rock, paper, scissors")
    print("9. Guess a number 1-9")

    ex = input("Which exercise do you want to run: ")
    globals()['exercise' + ex]()
