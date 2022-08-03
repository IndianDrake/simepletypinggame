import random, time
from colorama import Fore

wrd_list = list()
used_wrds = list()

wrds = open("words.txt")
for line in wrds: wrd_list.append(line.strip())

def pick_wrd():
    wrd = random.choice(wrd_list)
    used_wrds.append(wrd)
    return wrd

def user_type():
    return input("")

def start_game():
    print("Get Ready to Start!")
    time.sleep(.25)
    print("3")
    time.sleep(.25)
    print("2")
    time.sleep(.25)
    print("1")
    print(pick_wrd())

start_game()

start_time = time.time()

while True:
    user_input = user_type()
    last_wrd = used_wrds[len(used_wrds) - 1]

    if user_input == "":
        finish_time = time.time()
        time_taken = round((finish_time - start_time), 1)
        
        print(Fore.WHITE + "TIME TAKE: " + str(time_taken))
        print(Fore.WHITE + "TOTAL WORDS: " + str(len(used_wrds)))
        print(Fore.WHITE + "WPM: " + str(round((len(used_wrds) * 60/time_taken), 1)))
        break
    elif user_input == last_wrd:
        print(Fore.WHITE + pick_wrd())
    else:
        print(Fore.RED + "Typo!")
