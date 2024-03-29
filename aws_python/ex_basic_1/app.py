import boto3

s3 = boto3.resource('s3','us-east-1').meta.client

ssm = boto3.client('ssm','us-east-1')

bucket_name = ssm.get_parameter(Name='dragon_data_bucket_name',WithDecryption=False)['Parameter']['Value']
file_name = ssm.get_parameter(Name='dragon_data_file_name',WithDecryption=False)['Parameter']['Value']

def list_dragons():
    expression = "select * from s3object s"
    result = s3.select_object_content(
        Bucket=bucket_name,
        Key=file_name,
        ExpressionType='SQL',
        Expressions=expression,
        InputSerialization={'JSON': {'Type': 'Document'}},
        OutputSerialization={'JSON': {}}
    )
    
    for event in result['Payload']:
        if 'Records' in event:
            print(event['Records']['Payload'].decode('utf-8'))
            
list_dragons()