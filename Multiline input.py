print ("Enter the Multiline input, but click the Enter tab once when you have to go next line... once completed, click enter twice")
text = ""
line = input()
while line != "":
    text+= line + "\n"
    line = input()
print (text)
