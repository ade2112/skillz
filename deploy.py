import os
import click
import smtplib, ssl

emails = ['solomonmarvel@hotmail.com']

config = {
        "port" : 587,
        "smtp_server" : "smtp.sendgrid.net",
        "sender_email" : "storm@tosoptech.com",
        "username": "apikey",
        "password" : "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",
}


@click.command()
@click.option("--message", prompt="Deployment Comment", help="The person to greet.")
def deploy(message):
    """Deployment process"""
    print('pushing to github')
    os.system("npm run build") # build project
    os.system("git add .")    # add all to git
    os.system(f"git commit -m '{message}'") # commit deployment
    os.system("git push") # push staging code
    print("successful")
    os.system("rm -r dist") # delete build directory
    # os.system("cd .. && rm -r dist") # delete build directory
    # send_mail(emails, message)

def send_mail(emails, message):
    body = f'A new deployment was made with tag => {message}'
    content = f'From: {config["sender_email"]}\nSubject: New Staging Deployment\n\n{body}'

    context = ssl.create_default_context()
    # send mail
    with smtplib.SMTP(config["smtp_server"], config["port"]) as server:
        try:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(config["username"], config["password"])
            for receiver_email in emails:
                server.sendmail(config["sender_email"], receiver_email, content)
            print("Mail sent successfully")
            os.system("npm run serve") # serve local project
        except Exception as e:
            # Print any error messages to stdout
            print(e)
        finally:
            server.quit()

if __name__ == '__main__':
    deploy()