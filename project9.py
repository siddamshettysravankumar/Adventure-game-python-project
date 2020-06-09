import time
import random


def print_time(message):
    print(message)
    time.sleep(1)


def win():
    print("you won great choice!")


def dead():
    print("you lost the game")


def forest():
    print_time("Now you entred into the forest\n"
               "In front of you there is a lion")
    run = input("1.Fight\n"
                "2.runway\n")
    if "1" == run:
        print_time("Lion killed you and you are dead")
        dead()
    elif "2" == run:
        print_time("you will go deep into forest\n"
                   "You will find box")
        box = input("1.open\n"
                    "2.ignore\n")
        if "1" == box:
            print_time("you got tresure\n")
            win()
        elif "2" == box:
            print_time("you dont get tresure\n")
            dead()
        else:
            print_time("you are dead.Try again")
            dead()
    else:
        print_time("you are dead.Try again")
        dead()


def lava():
    print_time("you have chossen lava \n"
               "Due to over heat\n")
    print_time("you are dead")


def land():
    print_time("you have choosen Land")
    print_time("Now you have two ways to go")
    print_time("pick a number")
    in_land = input("1.If you Turn left you will go to Forest\n"
                    "2.If you turn right you will go to Desert\n")
    if "1" == in_land:
        forest()
    elif "2" == in_land:
        print_time("now you entred into Desert\n"
                   " you are tired, try to live and find way to tresure\n")
        water = input("1.water\n"
                      "2.Giveup\n")
        if "1" == water:
            print_time("drink some water and try for tresure\n"
                       "after some time youself find in forest")
            forest()
        elif "2" == water:
            print_time("you are dead")
            dead()
        else:
            dead()
    else:
        dead()


def water():
    print_time("Now you find youself in water\n")
    boat_start = input("1.boat\n"
                       "2.submarine\n")
    if "1" == boat_start:
        print_time("Now you have taken boat to go a head\n"
                   "you will be saling in water\n"
                   "killer fish attaked the boad\n"
                   "And you are dead\n")
        dead()

    if "2" == boat_start:
        print_time("now you are in submarine\n"
                   "sharks are getting near\n")
        sub = input("1.Fight\n"
                    "2.Turn back\n")
        if "1" == sub:
            print_time("shoot the shark and kill them\n"
                       "and will kill all the shark and go deep\n"
                       "you will find dimonds\n"
                       "and you will win\n")
            win()
        elif "2" == sub:
            print_time("you wont find tresure\n"
                       "you will loose")
            dead()
        else:
            print_time("you are dead")
            dead()
    else:
        print_time("you are dead")
        dead()


def story():
    print_time("Welcome to the adventuar game")
    print_time("Your are going to find Dimonds or Tresure")
    print_time("pick a name")
    a = ("Bob", "Jhon", "Rick", "Mike")
    random.choice(a)
    print_time(random.choice(a) + " you traped in a Old Temple")
    while True:
        print_time("you have three ways now")
        print_time("pick a number")
        start = input(" 1. If you choose to go front there is Lava \n"
                      " 2. If you choose to go right there is Land \n"
                      " 3. If you choose to go left there is river \n")
        if "1" == start:
            lava()
            break
        elif "2" == start:
            land()
            break
        elif "3" == start:
            water()
            break
        else:
            dead()
    print_time("Do you want to try again")
    try_again = input("1.yes\n"
                      "2.no\n")
    if "1" == try_again:
        story()
    elif "2" == try_again:
        print_time("hope you enjoyed the game\n"
                   "Thankyou")
    else:
        story()


story()
