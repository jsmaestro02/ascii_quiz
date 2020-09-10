import random

def main():
    life = 255
    score = 0
    while life > 0:
        ascii = random.randint(32,126)
        ch = chr(ascii)
        print(ch)
        guess = int(input("What is the ASCII code for this character? "))
        if guess == ascii:
            score += 1
            print("Correct!")
        else:
            life -= ascii
            if life < 0:
                print("Game Over!")
                print("Score:{}".format(score))
                i = input("Do you want to play again:(y/n)")
                if i == "y":
                    life = 255
                    score = 0
                    print("================================================")
                else:
                    return 0
                
            else:
                print("False!")
                print("Score:{}".format(score))
                print("{0} life remaining".format(life))
                print("-------------------------------------------")
               


main()
