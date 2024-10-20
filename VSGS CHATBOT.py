print ("VSGS CHATBOT")
while True:
    print()
    
    a = "BOT: "
    b = "YOU: "
    print (f'''{a} Hey there! How can I help you?
     Choose anyone:
            1. Admission Details
            2. Fee Structure
            3. Cirriculum / Syllabus
            4. Connect to an expert''')
    c = input(f'{b}'). lower()
    print ()
    if (c == "1") or c==("admission details") or (c=="admission"):
        print (f"""{a} Admission details:
        Currently Vijayadasami offer is going on!!

        Visit our School 'insert location' to know more details...""")
        print ()     
        print (f"{a} Anything Else do you need to know? (yes/no)")
        print ()
        e = input (f"{b}").lower()
        if e == "yes":
            continue
        elif e == "no":
            print ()
            print (f"{a}Have a Great day!! Byee!")
            break
        else:
            print ()
            print (f"{a} Connecting Back")
            continue

    elif (c == "2") or (c== "fee structure") or (c=="fees") or (c == "fee"):
        print (f"""{a} Fee Structure:
        Pre-KG - 5: Rs.50,000
        6 - 9 : 60,000
        10 - 12 : 75,000""")
        print ()
        print (f"{a} Anything Else do you need to know? (yes/no)")
        print ()
        e = input (f"{b}").lower()
        if e == "yes":
            continue
        elif e == "no":
            print ()
            print (f"{a}Have a Great day!! Byee!")
            break
        else:
            print ()
            print (f"{a} Connecting Back")
            continue

    elif (c == "3") or (c== "cirriculum") or (c=="syllabus"):
        print (f"""{a} Curriculum:
        Syallabus Followed : CBSE
        To know more about syllabus and curriculum please visit:
            'Insert Link' """)
        print ()
        print (f"{a} Anything Else do you need to know? (yes/no)")
        print ()
        e = input (f"{b}").lower()
        if e == "yes":
            continue
        elif e == "no":
            print ()
            print (f"{a}Have a Great day!! Byee!")
            break
        else:
            print ()
            print (f"{a} Connecting Back")
            continue


    elif (c == "4") or (c== "connect to an expert") or (c=="connect to expert") or (c == "connect expert") or (c == "connect") or (c == "expert"):
        print (f"""{a} Connecting you to an expert... This may take some time...""")
        print ()
        print (f"{a}Want to connect to an expert?? (yes/ no)")
        print ()
        d = input (f"{b}").lower()
        if d=="yes":
            print ()
            print (f"""{a} Connecting you to an expert... This may take some time...""")
            break
        elif d == "no":
            print ()
            print (f"{a}You are talking to VSGS BOT...")
            continue
        else:
            print ()
            print (f"{a}You are talking to VSGS BOT...")
            print ()
    else:
        print ()
        print ("Invalid Statement... Kindly Choose valid")
print ()
