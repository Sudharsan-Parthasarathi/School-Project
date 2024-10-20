while True:
    student = {"2029": "stud1", "2027":"Stud2", "2026": "Stud3"}
    teacher = {"1001": "Teacher1", "1002": "Teacher2", "1003": "Teacher3","1004": "Teacher4","1005": "Teacher5","1006": "Teacher6", }

    login = input ("Enter Login id: ")
    if login in student:
        print (f"Hey, {student[login]}. How are you doing today?")
        break
    elif login in teacher :
        print (f"Greetings, {teacher[login]}!")
        break
    else:
        print ("Login Failed... Try again...")
        continue
    
if login in teacher:
    print("""Choose the stream to upload homework:
        1.Science
        2.Commerce""")
    stream = input ("Enter: ").lower()
    if (stream == '1')or (stream == "science") or (stream == "sci"):
        while True:
            print ("Enter Homeworks(click enter tab twice when completed)- ")
            homework = ""
            line = input()
            while line != "":
                homework+= line + "\n"
                line = input()
            print (homework)
            update = input ("Want to update the homework? (yes / no): ").lower()
            if update== "yes":
                continue
            else:
                break

    if (stream == '2')or (stream == "commerce") or (stream == "arts"):
        while True:
            print ("Enter Homeworks(click enter tab twice when completed)- ")
            homework2 = ""
            line = input()
            while line != "":
                homework2+= line + "\n"
                line = input()
            print (homework2)
            update = input ("Want to update the homework? (yes / no): ").lower()
            if update== "yes":
                continue
            else:
                break
if login in student:
    print (f"Hey, {student[login]}. Choose your stream??")
    print ("""1. Science
2. Commerce/Arts""")
    i = input ("Enter: ").lower()
    if i == "science" or i == "sci" or i == "1":
        question= input ("You: ")
        q = list (question)
        if "homework" or "hw" in q:
            print (homework)
    if i == "commerce" or i == "arts" or i == "2":
        question= input ("You: ")
        q = list (question)
        if "homework" or "hw" in q:
            print (homework2)

#else we can add the homeworks manually

#need to upload timetable, circular, test
