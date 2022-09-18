import boto3

client = boto3.client('s3')

response = client.list_objects(Bucket='aws-bma-test')

for content in response['Contents']:
    object_dict = client.get_object(Bucket='aws-bma-test', Key = content['Key'] )
    print(content['Key'], object_dict)