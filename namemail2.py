import smtplib
import getpass
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 


s=smtplib.SMTP('smtp.gmail.com','587')
s.starttls()
sender='nagarjunn214@gmail.com'
receiver='imnnagarjun4@gmail.com'
msg = MIMEMultipart() 
body="Hi, I have attached the file below"
msg.attach(MIMEText(body,'plain')) 
filename="namfunc.py"
attachment = open("home/Desktop/NamithaBL1/namfunc.py", "rb")
p = MIMEBase('application', 'octet-stream')  
p.set_payload((attachment).read()) 
encoders.encode_base64(p) 
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
msg.attach(p) 	
p=getpass.getpass()
s.login(sender,p)
s.sendmail(sender,receiver,msg)
print("msg sent successfully!!")
s.quit()