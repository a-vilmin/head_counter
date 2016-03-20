import tkinter
import smtplib
import time, sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail():
    fp = open(sys.argv[1], 'r')
    info = [x.strip('\n') for x in fp.readlines()]
    
    msg = MIMEMultipart()
    msg['From'] = info[0]
    msg['To'] = info[1]
    msg['Subject'] = "Head Count for Blind Pig, " + time.strftime("%x")   
    
    body = "The head count for tonight was "+enter.get()+"\n Thanks,\nAdam"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(info[0], info[2])
    txt = msg.as_string()
    server.sendmail(info[0], info[1], txt)
    server.quit()
    
top = tkinter.Tk()
top.title("Head Count Email")

lbl = tkinter.Label(top, text= "How many people tonight?")
enter = tkinter.Entry(top)
btn = tkinter.Button(top, text= "Send Email", command=send_mail)

lbl.pack()
enter.pack()
btn.pack()


top.mainloop()


