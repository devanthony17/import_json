import json
import boto3

# Define a bucket in S3 where we will store the student's result data
s3_bucket_name = 'your-s3-bucket-name'
s3 = boto3.resource('s3')

# Function to create a unique file name for the student's result data
def create_unique_filename(student_id):
    return f'{student_id}_results.json'

# Function to upload a student's result data to S3
def upload_student_result(student_id, result):
    # Create a unique file name for the student's result data
    filename = create_unique_filename(student_id)

    # Convert the result data into a JSON string
    result_json = json.dumps(result)

    # Upload the result data to the S3 bucket
    s3.Bucket(s3_bucket_name).put_object(Key=filename, Body=result_json)

# Function to get a student's result data from S3
def get_student_result(student_id):
    # Create a unique file name for the student's result data
    filename = create_unique_filename(student_id)

    # Get the result data from the S3 bucket
    response = s3.Bucket(s3_bucket_name).get_object(Key=filename)

    # Convert the result data from a JSON string to a Python dictionary
    result = json.loads(response['Body'].read().decode('utf-8'))

    return result

# Example usage
upload_student_result(1, {'math': 85, 'science': 90, 'history': 92})
print(get_student_result(1))