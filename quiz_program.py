quiz = {
    "1. ": {
        "question" : "What is the capital of Ghana?",
        "answer" : "Accra"
        },
    "2. " : {
        "question" : "Ghana is on which continent?",
        "answer" : "Africa"
        },
    "3. " : {
        "question" : "Which year did Ghana gain independence?",
        "answer" : "1957"
        },
    "4. " : {
        "question" : "Kejetia Market is in which city?",
        "answer" : "Kumasi"
        }
    }
score = 0
print("WELCOME TO AGOROO", "\n")
for key, value in quiz.items():
    print(key, value['question'])
    answer = input('Answer : ')
    if answer.lower() == value['answer'].lower():
        score = score + 3
        print("Correct for 3 points")
        print("Score : ", score, "\n")
    else:
        print("Opps! ", answer, " is wrong. The correct answer is ", value['answer'])
        print("Score : ", score, "\n")

print("Final score : ", score)
print("Total percentage : ", str(int(score / 12 * 100)))

