""" 
1) Replace 'Source' email address with your Amazon SES-verified sender email address in the same AWS account and Region.
2) Click 'Deploy' button on the Toolbar.
3) Once the deployment is successful, copy the API endpoint URL from the output parameter section of Deployment Summary 
view or via the 'Deployment' tab of 'Project' → 'Show Info'.
4) Using an HTTP client, make a POST request to the above API endpoint URL.
(Refer https://www.slappforge.com/blog/set-email-reminders-to-reduce-shopping-cart-abandonment for more details)
"""

import boto3
ses = boto3.client("ses")

def handler(event, context):   
    print(event)
    
    tabledetails = event["Records"][0]["dynamodb"]
    print(tabledetails)
    
    name = tabledetails["NewImage"]["Name"]["S"];
    email = [tabledetails["NewImage"]["Email"]["S"]];
    url = tabledetails["NewImage"]["URL"]["S"];
    messagebody = """Hi %s!
    
Your shopping cart on Online-Business is waiting for you.
Follow this link to return to your cart:
    
%s""" % (name, url)

    try:
        data = ses.send_email(
            Source="sender@example.com",
            Destination={
                'ToAddresses': email
            },
            Message={
                'Subject': {
                    'Data': "Your cart is waiting!"
                },
                'Body': {
                    'Text': {
                        'Data': messagebody
                    }
                }
            }
        )
        print("Email sent!")
        return {"message": "Successfully executed"}

    except BaseException as e:
        print(e)
        raise(e)