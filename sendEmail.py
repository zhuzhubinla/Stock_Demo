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
        smtp.login('zhu.zhubinlala@gmail.com','*****')
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
    
    
import datetime
today=datetime.date.today()
yesterday=today-datetime.timedelta(days=1)
tomorrow=today+datetime.timedelta(days=1)


import datetime,calendar
last_friday=datetime.date.today()
oneday=datetime.timedelta(days=1)
while last_friday.weekday!=calendar.FRIDAY:
    last_friday-=1
    


import datetime 
import calendar 
    
today = datetime.date.today() 
target_day = calendar.FRIDAY 
this_day = today.weekday() 
delta_to_target = (this_day - target_day) % 7
last_friday = today - datetime.timedelta(days = delta_to_target)  



import time,os
ef repeat_run(cmd,sleepTime=60):
	while True:
		os.system(cmd)
		time.sleep(sleepTime)

		
repeat_run("print('test')",5)



    
//sched       
import datetime,time,sched
def event_function(msg):
	print('Message: %s recived at%s'%(msg,time.strftime('%Y-%m-%d:%H:%M:%S',time.localtime(time.time())))

if “__name__”==”__main__“:
	s=sched.scheduler(time.time,time.sleep)
	s.enter(1,1,event_function,('test',))



def split_function(orig,split_cha):
    split_txt=orig.split(split_cha)
    print(split_txt)
    if len(split_txt)>1:
        for i in range(0,len(split_txt)):
            if split_txt[i]!='':
                split_txt[i]=split_txt[i][0].upper()+split_txt[i][1:]
                print(split_txt[i])
            else:
                continue
        return ' '.join(split_txt)
    else:
        return orig






    
    
    
