print("=====QUIZ APPLICATION======")
questions = ["\n1.What is the capital of India?",
             "\n2.How many days are there in a week?",
             "\n3.What is the largest planet in our solar system?",
             "\n4.Which programming language are we using?",
             "\n5.What is 4*4?",
             "\n6.What is the national animal of India?",
             "\n7.How many months are there in a year?"]
answers  = ["delhi",
    "7",
    "jupiter",
    "python",
    "16",
    "tiger",
    "12"]

score=0
for i in range(len(questions)):
    print(questions[i])
    user_answer=input("Enter your answer:").lower()
    if user_answer==answers[i]:
        print('You are correct')
        score+=1
    else:
        print('You are incorrect')
        print("Correct answer:", answers[i])
percentage=(score/len(questions))*100

def display_result():
    print("======FINAL RESULT======")
    print("Final score is:",score,'/',len(questions))
    print("Total percentage is:",round(percentage,2))
    print("Thank you for using QUIZ APPLICATION")
display_result()
