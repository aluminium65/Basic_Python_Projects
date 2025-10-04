import random

print("""

 @@@@  @   @ @@@@ @@@@ @@@@ @@@@ @@@
@      @   @ @    @    @    @    @  @
@   @@ @   @ @@@@ @@@@ @@@@ @@@@ @@@
@    @ @   @ @       @    @ @    @ @
@@@@@@  @@@  @@@@ @@@@ @@@@ @@@@ @  @


----------------------By aluminium--------------------------      


""")
print("[GITHUB] https://github.com/aluminium65/")

answer = random.randint(1,100)
guess = 0


print("Guess the number between 1 to 100.")

enter = input("  >> ")
enter = int(enter)


while enter != answer:
    print("Wrong!")
    guess += 1

    if enter > answer:

            if enter - 15 <= answer:
                print("you're a bit high.")

                enter = input("  >> ")
                enter = int(enter)

            else:
                print("you're too High")

                enter = input("  >> ")
                enter = int(enter)


    if enter < answer:

            if enter + 15 >= answer:
                print("you're a bit low.")

                enter = input("  >> ")
                enter = int(enter)

            else:
                print("Too Low")

                enter = input("  >> ")
                enter = int(enter)

if enter == answer:
    print("Congrats! You got it right")
    print(f"It took you {guess} guesses!")


match guess:
    case 1|2|3:
        print("True Mind Reader, you are!")
    case 4|5|6:
        print("Not Bad")
    case _:
        print("You should work on your common sense!")
