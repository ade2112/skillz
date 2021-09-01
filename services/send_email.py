import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText




async def send_email(sender_email:str,password:str,receiver_email:str,mail_subject:str,message:str):  
    try:
        server=smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(sender_email,password)    
        msg = MIMEMultipart()
        msg['From']=send_email
        msg['To']= receiver_email
        msg['Subject']= mail_subject

        msg.attach(MIMEText(message, 'html'))
        server.send_message(msg)
        server.quit()
        print("mail sent")
    except Exception as e:
        print (e)

