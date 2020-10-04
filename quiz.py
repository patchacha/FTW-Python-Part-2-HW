# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 20:18:56 2020

@author: ppangatungan
"""

#Multiple Choice Questions with answers that prints top 10 scorers and is able to do CRUD

import json 

#function to answer the quiz 
def answerquiz(name):
    point = 0
    #Open for reading and writing, starts at beginning of file 
    with open("files/quizquestions.json", 'r+') as f:
        q = json.load(f) #loads data in q 
        lengthquestions = len(q) #determine number of questions 
        #prints the questions, choices and gets the answer 
        for i in range(lengthquestions):
            print(f'\n{i+1}. {q[i]["question"]}\n')
            for choice in q[i]["choices"]:
                print(choice)
            answer = input("\nAnswer: ")
            #compares answer with correct answer, error handling - always comparing capital letters 
            if q[i]["answer"][0] == answer[0].upper():
                point+=1
        
        #rating of score
        percentage = int((point/lengthquestions)*100)
        
        #printing results 
        print('\nHi '+ name.title() + '!')
        if percentage >= 70:
            print("\nCongratulations!\nYou know the Philippines so well!\nYou got "+ str(int(point)) + " over " + str(lengthquestions) + " or " + str(percentage) + "%\n")
        else:
            print("Oh no. You still have a lot to learn about our country.\nYou got "+ str(int(point)) + " over " + str(lengthquestions) + " or " + str(percentage) + "%\n") 
        
        #writing users and scores in a txt file separated by ; 
        scorefile = open("userscores.txt","a") #append and adds at the last part of the code 
        scorefile.write(name.title() + ";" + str(point) + "\n")
        scorefile.close()

        #reading and printing previous users and scores 
        print("Here are the scores of the previous top 10 quiz takers:\n")
        readscore = open("userscores.txt","r")
        name_score = [] #empty list for name and score tandem 
        #reads user and score by finding ; 
        for line in readscore:
            name, score = line.split(";")[0], float(line.split(";")[1])
            name_score.append((name, score))
        #sort scores in ascending order 
        name_score.sort(key = lambda t: t[1], reverse=True)
        #print leaderboard (top 10)
        for i, (name,score) in enumerate(name_score[:10]):
            print("{}. {} - {}".format(i+1, name.title(), int(score)))
        readscore.close()
            
def addquestions():
    #input prompt for new question
    newquestion = input("Type the question you would like to add:\n")
    print("\nEnter the choices:")
    #input prompt for choices 
    choiceA = input('A: ')
    choiceB = input('B: ')
    choiceC = input('C: ')
    #putting the choices in a list 
    newchoices = ['A. ' + choiceA, 'B. '+ choiceB, 'C. '+ choiceC]
    #input prompt for answer
    newanswer = input('Enter the answer: ')
    
    with open("files/quizquestions.json", 'r+') as f: 
        q = json.load(f)
        #putting questions,choice and answer in dictionary
        newq = {"question": newquestion, "choices": newchoices, "answer": newanswer}
        #appending dictionary to list of questions 
        q.append(newq)
        #sets the reference point at the beginning of the file
        f.seek(0)
        json.dump(q, f)
        f.truncate() #clears file
    
    print("\nThanks for adding a question!\n")
    
def deletequestions():
    with open("files/quizquestions.json", 'r+') as f:
        q = json.load(f)
        lengthquestions = len(q)
        print("\n\nHere are the list of questions:\n")
        #prints questions 
        for i in range(lengthquestions):
            print(f'{i+1}. {q[i]["question"]}')
        #input prompt of question number to delete
        delq = int(input('Which question would you like to delete? Pick a number from 1 to ' + str(lengthquestions) +': '))
        for i in range(lengthquestions):
            if i+1 == delq:
                del q[i] #delete question number chosen 

        with open("files/quizquestions.json", 'w') as fnew:
            fnew.write(json.dumps(q))
            
def updatequestions():
    with open("files/quizquestions.json", 'r+') as f:
        q = json.load(f)
        lengthquestions = len(q)
        print("\n\nHere are the list of questions:\n")
        for i in range(lengthquestions):
            print(f'{i+1}. {q[i]["question"]}')
        updq = int(input('Which question would you like to update? Pick a number from 1 to ' + str(lengthquestions) +': '))
        updatedquestion = input("Type the updated question:\n")
        print("\nEnter the choices:")
        #input prompt for choices 
        updchoiceA = input('A: ')
        updchoiceB = input('B: ')
        updchoiceC = input('C: ')
        #putting the choices in a list 
        updchoices = ['A. ' + updchoiceA, 'B. '+ updchoiceB, 'C. '+ updchoiceC]
        #input prompt for answer
        updanswer = input('Enter the answer: ')
        updques = {"question": updatedquestion, "choices": updchoices, "answer": updanswer}
        for i in range(lengthquestions):
            if i+1 == updq:
                q[i]["question"] = updatedquestion
                q[i]["choices"] = updchoices
                q[i]["answer"] = updanswer
        f.seek(0)
        json.dump(q, f)
        f.truncate() #clears file
        
    print("\nThanks for updating a question!\n")
        
if __name__ == "__main__":
    choice = 1
    name = input("Please enter your name: ")
    print('\nHello ' + name.title() + '! Welcome to a Quiz about the Philippines: How well do you know our country?')
    while choice != 5:
        choice = int(input('What do you want to do?\n1. ANSWER QUIZ\n2. ADD QUESTION\n3. DELETE QUESTION\n4. UPDATE QUESTION\n5. QUIT\n\nCHOICE: '))
        if choice == 1:
            answerquiz(name)
        elif choice == 2:
            addquestions()
        elif choice == 3:
            deletequestions()
        elif choice == 4:
            updatequestions()
        elif choice == 5:
            print('\nOkay, bye!')
            break
        else:
            print('\nWrong input. Please choose between numbers 1 to 4 only.')

