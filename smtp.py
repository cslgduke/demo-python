import smtplib
from email.mime.text import MIMEText
from email.header import Header


mail_host="smtp.163.com"  #设置服务器
mail_user="cslgduke@163.com"    #用户名
mail_pass="JLXLUKPYWLCUZWVQ"   #口令


sender = 'cslgduke@163.com'
receivers = ['cslgduke@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("Python robot", 'utf-8')   # 发送者
message['To'] =  Header("测试", 'utf-8')        # 接收者

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')


try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")