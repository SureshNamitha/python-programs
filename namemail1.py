import smtplib
import getpass

s=smtplib.SMTP('smtp.gmail.com','587')
s.starttls()
sender='nagarjunn214@gmail.com'
receiver='imnnagarjun4@gmail.com'
msg="HI HOW R U??"
p=getpass.getpass()
s.login(sender,p)
s.sendmail(sender,receiver,msg)
print("msg sent successfully!!")
s.quit()