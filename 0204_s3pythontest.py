import boto3
s3 = boto3.client("s3")

def handler(event, context):
    try:
        data = s3.list_objects(
            Bucket="as2-test-lahiru",
            MaxKeys=10
        )
    except BaseException as e:
        print(e)
        raise(e)
    
        try:
            data = s3.put_object(
                Bucket="hiru.0204",
                Key="sample.txt",
                Body="test123",
                Metadata={}
            )
        except BaseException as e:
            print(e)
            raise(e)

    
    return {"message": "Successfully executed"}
