import smtplib, ssl


smtp_server= "smtp-mail.outlook.com"
port= 587
sender_email= "mecmaharshi9@hotmail.com"
password= "testing@123"
receiver_mail = "mecmaharshi9@gmail.com"

subject= "Test mail from Python"
content= " hi there this is a test mail using python"
msg = 'Subject:' + subject + '\n\n' + content

context = ssl.create_default_context()

try:
    server =smtplib.SMTP(smtp_server, port)
    server.starttls(context = context)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_mail, msg)
    print("mail sent ;)")
except Exception as e:
    print(e)

server.quit()
