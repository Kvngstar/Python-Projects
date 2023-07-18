#dictionary to store the questions  and answers 

#loop through the dictionary and ask the user the questions
#check if the answer is correct
#keep track of the score
#display the score at the end of the quiz


dict = {"What is the capital of the United States?": "Washington",
        "How many number of States in US": "50", 
        "What is the capital of france":"paris"}
total = 0
for x in dict:
    answer = input(f"{x}: ")
    if answer == dict[x]:
        total = total + 1
        print("Correct!")
        print(f"Your Total score is {total}")
    else:
        print("Wrong!")
print(f"You scored is: {total}  out of {len(dict)}")
 