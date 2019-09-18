from random import randint
from banner import banner

banner("rock, paper, scissors", "Russell")

print("we are going to play rock, paper,scissors. the first one to win two out of 3 rounds is the winner")
pscore = 0
cscore = 0

while pscore < 2 and cscore < 2:
    player = int(input("1= Rock,2= Paper,or 3= Scissors?"))
    computer=randint(1,3)
    if player == computer:
         print("Tie!")
    elif player == 1:
        if computer == 2:
            print(f"you lose, paper covers rock")
            cscore = cscore + 1
        else:
            print(f"you win! rock smashes scissors")
            pscore = pscore +1
    elif player == 2:
        if computer == 3:
            print(f"you lose! scissors cuts paper")
            cscore = cscore +1
        else:
            print(f"you win!,paper covers rock")
            pscore = pscore +1
    elif player == 3:
        if computer == 1:
            print(f"you lose! rock smashes scissors")
            cscore = cscore +1
        else:
            print(f"you win! scissors cut paper")
            pscore = pscore +1
    else:
        print("thats not a valid play please check your spelling")
if pscore >= 2:
    print("you have defeated the computer!")
elif cscore >= 2:
    print("The computer beat you!")
















