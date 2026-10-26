key = input("Enter answer key: ").upper()
answers = input("Enter student answers: ").upper()

if len(key) != len(answers):
    print("Answer count does not match")
else:
    correct = 0
    wrong = 0
    unanswered = 0

    for i in range(len(key)):
        if answers[i] == "-":
            unanswered += 1
        elif answers[i] == key[i]:
            correct += 1
        else:
            wrong += 1

    score = correct * 1 - wrong * 0.25

    print("Correct Answers:", correct)
    print("Wrong Answers:", wrong)
    print("Unanswered:", unanswered)
    print("Final Score:", score)