# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 20:18:56 2020

@author: ppangatungan
"""

#Multiple Choice Questions with answers that prints top 10 scorers and is able to do CRUD

import json 

def answerquiz(name):
    point = 0
    with open("files/quizquestions.json", 'r+') as f:
        q = json.load(f)
        lengthquestions = len(q)
        for i in range(lengthquestions):
            print(f'\n{i+1}. {q[i]["question"]}\n')
            for choice in q[i]["choices"]:
                print(choice)
            answer = input("\nAnswer: ")
            if q[i]["answer"][0] == answer[0].upper():
                point+=1
                
        percentage = int((point/lengthquestions)*100)

        print('\nHi '+ name.title() + '!')
        if percentage >= 70:
            print("\nCongratulations!\nYou know the Philippines so well!\nYou got "+ str(int(point)) + " over " + str(lengthquestions) + " or " + str(percentage) + "%\n")
        else:
            print("Oh no. You still have a lot to learn about our country.\nYou got "+ str(int(point)) + " over " + str(lengthquestions) + " or " + str(percentage) + "%\n") 

        scorefile = open("userscores.txt","a")
        scorefile.write(name.title() + ";" + str(point) + "\n")
        scorefile.close()

        #reading and printing previous users and scores 
        print("Here are the scores of the previous top 10 quiz takers:\n")
        readscore = open("userscores.txt","r")
        name_score = []
        for line in readscore:
            name, score = line.split(";")[0], float(line.split(";")[1])
            name_score.append((name, score))
            #data = line.split(";")
            #print(data[0]+ " - "+ data[1], end="")
        name_score.sort(key = lambda t: t[1], reverse=True)    
        for i, (name,score) in enumerate(name_score[:10]):
            print("{}. {} - {}".format(i+1, name.title(), int(score)))
        readscore.close()
            
def addquestions():
    newquestion = input("Type the question you would like to add:\n")
    print("\nEnter the choices:")
    choiceA = input('A: ')
    choiceB = input('B: ')
    choiceC = input('C: ')
    newchoices = ['A. ' + choiceA, 'B. '+ choiceB, 'C. '+ choiceC]
    newanswer = input('Enter the answer: ')
    
    with open("files/quizquestions.json", 'r+') as f: 
        q = json.load(f)
        newq = {"question": newquestion, "choices": newchoices, "answer": newanswer}
        q.append(newq)
        f.seek(0)
        json.dump(q, f)
        f.truncate()
    print("\nThanks for adding a question!\n")
    
def deletequestions():
    with open("files/quizquestions.json", 'r+') as f:
        q = json.load(f)
        lengthquestions = len(q)
        print("\n\nHere are the list of questions:\n")
        for i in range(lengthquestions):
            print(f'{i+1}. {q[i]["question"]}')
        delq = int(input('Which question would you like to delete? Pick a number from 1 to ' + str(lengthquestions) +': '))
        for i in range(lengthquestions):
            if i+1 == delq:
                del q[i]

        with open("files/quizquestions.json", 'w') as fnew:
            fnew.write(json.dumps(q))

if __name__ == "__main__":
    choice = 1
    name = input("Please enter your name: ")
    print('\nHello ' + name.title() + '! Welcome to a Quiz about the Philippines: How well do you know our country?')
    while choice != 4:
        choice = int(input('What do you want to do?\n1. ANSWER QUIZ\n2. ADD QUESTIONS\n3. DELETE QUESTIONS\n4. QUIT\n\nCHOICE: '))
        if choice == 1:
            answerquiz(name)
        elif choice == 2:
            addquestions()
        elif choice == 3:
            deletequestions()
        elif choice == 4:
            print('\nOkay, bye!')
            break
        else:
            print('\nWrong input. Please choose between numbers 1 to 4 only.')

