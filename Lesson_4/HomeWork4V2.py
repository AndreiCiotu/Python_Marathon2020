from Question import Question

f = open("countries.txt") 
Content = f.read() 
CoList = Content.split("\n")
import random
RC1 = random.choice(CoList)
a = RC1.split(",")
RC1 = random.choice(CoList)
b = RC1.split(",")
RC1 = random.choice(CoList)
c = RC1.split(",")
RC1 = random.choice(CoList)
d = RC1.split(",")
RC1 = random.choice(CoList)
e = RC1.split(",")
RC1 = random.choice(CoList)
n = RC1.split(",")
question_prompts1 = 'Care este capitala la ' ,a[0],"Variante de raspuns:","a-",d[1], "b-", e[1], "c-", b[1], "d-",a[1]
question_prompts2 = "Care este capitala la " ,b[0],"Variante de raspuns:","a",e[1], "b", b[1], "c",n[1], "d",c[1]
question_prompts3 = "Care este capitala la " ,c[0],"Variante de raspuns:","a",c[1], "(b)", n[1], "(c)",b[1], "(d)",a[1]

questions = [
    Question(question_prompts1,"d"),
    Question(question_prompts2,"b"),
    Question(question_prompts3,"a"),
   
]



def run_test(questions):
    score = 0
    for  question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("Ai acumulat "+ str(score) + " raspunsuri corecte din " + str(len(questions)))

run_test(questions)

