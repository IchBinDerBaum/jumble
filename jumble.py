import random
words = ["interference", "band", "requirement", "hesitate", "season", "shareholder", "crouch", "camera"]

while True:
    tries = 3
    word = random.choice(words)

    s = ""
    correct = word

    while word:
        position = random.randrange(len(word))
        s += word[position]
        word = word[:position] + word[position + 1:]
    while tries > 0:
        answer = input(f"What is this word: {s}").lower()
        if answer == correct:
            print("You got it right!")
            break
        elif answer != correct:
            print(f"That's not right. You have {tries} more tries")
            tries -= 1
    else:
        print(f"You loose :( The answer was {correct}")
    a = input("Do you want to play another game?").lower()
    if a == "yes":
        print("Are you ready?")
    else:
        print("Okay, have a good day!")
        break
