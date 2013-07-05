import email
import mimetypes
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from email.MIMEMultipart import MIMEMultipart
import smtplib
import time

def connection():
    try:
        smtp=smtplib.SMTP_SSL()
        smtp.connect('smtp.gmail.com',465)
        smtp.login('zhu.zhubinlala@gmail.com','160815zb@')
        #smtp.sendmail(mail_from,mail_to,msg.as_string())
        #smtp.quit()
        print 'ok'
    except exception,e:
        print e

    return smtp

def logout(smtp):
    smtp.quit()
    


def send_plaintext(smtp):
    mail_body='test message'
    mail_from='zhu.zhubinlala@gmail.com'
    mail_to=['allenbintestzhu@gmail.com']
    msg=MIMEText(mail_body)
    msg['Subject']='test email'
    msg['To']=';'.join(mail_to)
    msg['date']=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    smtp.sendmail(mail_from,mail_to,msg.as_string())



def send_emailwithattachment(connection):
    mail_body='test message'
    mail_from='zhu.zhubinlala@gmail.com'
    mail_to=['allenbintestzhu@gmail.com']
    msg=MIMEMultipart()
    msg['Subject']='test email'
    msg['To']=';'.join(mail_to)
    msg['date']=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    txt=MIMEText('test message')
    msg.attach(txt)
    picPath=['E:/new/a.png']
    for img in picPath:
        pic=open(img,'rb')
        readPic=MIMEImage(pic.read())
        msg.attach(readPic)
    try:
        smtp=smtplib.SMTP_SSL()
        smtp.connect('smtp.gmail.com',465)
        smtp.login('zhu.zhubinlala@gmail.com','160815zb@')
        smtp.sendmail(mail_from,mail_to,msg.as_string())
        smtp.quit()
        print 'ok'
    except exception,e:
        print e

if __name__ == '__main__':
    smtp=connection()
    for i in range(0,2,1):
        send_plaintext(smtp)
        #send_emailwithattachment()
        time.sleep(6)
    logout(smtp)
    
    
        
        
    
    
    
