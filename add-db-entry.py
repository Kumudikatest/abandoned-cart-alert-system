import boto3
ddb = boto3.client("dynamodb")

def handler(event, context):
    
    name = event['Name']
    email = event['Email']
    url = event['URL']

    try:
        data = ddb.put_item(
            TableName="history",
            Item={
                'Name': {
                    'S': name
                },
                'Email': {
                    'S': email
                },
                'URL': {
                    'S': url
                }
            }
        )
        print("Successfully Saved entry from email:"+ email)
        return {"message": "Successfully executed"}

    except BaseException as e:
        print(e)
        raise(e)