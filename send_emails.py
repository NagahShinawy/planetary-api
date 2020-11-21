import smtplib
from email.mime.text import MIMEText


def send_email(customer, dealer, rating, comments):
    port = 2525
    server = "smtp.mailtrap.io"
    username = "YOUR USERNAME"
    pwd = "YOUR PASSWORD"
    title = "<h1>New Feedback</h1>"
    info = f"""
    <ul>
        <li>Customer is : {customer}</li>
        <li>Dealer is : {dealer}</li>
        <li>Rating is : {rating}</li>
        <li>Your Comment is : {comments}</li>
    </ul>
    """
    sender = "nagah@huawei.com"
    receiver = "client@we.com"
    msg = MIMEText(title + info, 'html')
    msg['Subject'] = 'Client Feedback'
    msg['From'] = sender
    msg['to'] = receiver

    with smtplib.SMTP(server, port) as srv:
        srv.login(username, pwd)
        srv.sendmail(sender, receiver, msg.as_string())