questions = [
    ["Who is the CEO of Tesla?", "Elon Musk", "Jeff Bezos", "Bill Gates", "Sundar Pichai", 1],

    ["What is the capital of Japan?", "Beijing", "Seoul", "Tokyo", "Bangkok", 3],

    ["Which data structure uses FIFO?", "Stack", "Queue", "Tree", "Graph", 2],

    ["Which planet is called the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],

    ["Who developed Python programming language?", "James Gosling", "Dennis Ritchie", "Guido van Rossum", "Bjarne Stroustrup", 3],

    ["What does CPU stand for?", "Central Processing Unit", "Computer Personal Unit", "Central Program Utility", "Control Processing Unit", 1],

    ["Which company owns Instagram?", "Google", "Meta", "Twitter", "Snapchat", 2],

    ["What is the boiling point of water (°C)?", "90", "95", "100", "110", 3],

    ["Which language is mainly used for Android development?", "Swift", "Kotlin", "Python", "JavaScript", 2],

    ["What is the smallest unit of data in a computer?", "Byte", "Bit", "Nibble", "Word", 2]
]

prizes = [10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]

i = 0
for question in questions:
    
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")



    a = int(input("Enter your answer . 1 for a, 2 for b,3 for c ,4 for d\n"))
    if(question[5] == a):
        print("Correct answer")

    else:
        print("Incorrect answer\n The correct answer was", {question[5]})
        break
    print("You won",prizes[i])
    i +=1