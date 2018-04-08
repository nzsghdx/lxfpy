MUA:Mail User Agent(邮件用户代理)
MTA:Mail Transfer Agent(邮件传输代理)
MDA:Mail Delivery Agent(邮件传输代理)

电子邮件的旅程:发件人->MUA->若干个MTA<-MDA<-MUA<-收件人

编写程序实现发送和接收邮件的本质是:
1.编写MUA把邮件发送到MTA;
2.编写MUA从MDA上收取邮件;

>发送邮件时MUA和MTA使用的是SMTP协议:Simple Mail Transfer Protocol

>收取邮件时MUA和MDA使用的是POP3协议:POST Office Protocol和IMAP4:Internet Message Access Protocol

	>IMAP4的优点是不但能收取邮件,还可以直接操作MDA上存储的邮件,比如从收件箱移到垃圾箱.


发邮件时,首先配置smtp服务器,就是要发送到那个mta上,还要填写邮箱地址和密码,这样mua才能通过smtp协议发送到mta上.

收邮件时,从mda收取邮件,mda服务器也要求验证邮箱密码,这样mua才能顺利的通过pop或imap协议从mda上成功的收取邮件.





