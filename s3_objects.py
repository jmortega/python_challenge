import boto3

from aws_credential_helper import aws_credential_helper


class s3_objects:

    def __init__(self):
        '''
        Initialize a reusable, authenticated boto3 client for s3 in _s3_client
        Set the lab bucket name in _bucket 
        '''
        self._s3_client = aws_credential_helper.create_new_session().client('s3')
        self._bucket = self._get_lab_bucket()

    def _get_lab_bucket(self):
        response = self._s3_client.list_buckets()
        # Return the only bucket in the lab (or raise an exception if the bucket isn't created)
        return response['Buckets'][0]['Name']

    def _read_body(self, streaming_body):
        return streaming_body.read()

    def _decode_content_bytes_to_string(self, bytes):
        return bytes.decode('utf-8')

    def get_content(self, object_key):
        '''
        Return a string containing the content of the object represented by object_key.

        The object_key can be assumed to exist in the lab's bucket.
        Arguments
        object_key: The key of the desired object in the S3 bucket
        '''

        # ====================================
        # Do not change the code before this

        # CODE2: Write code that completes the function as described in the docstring
        object= self._s3_client.get_object(Bucket=self._bucket,Key=object_key)
        streaming_body = object['Body']
        bytes =  self._read_body(streaming_body)
        return self._decode_content_bytes_to_string(bytes)

if __name__ == '__main__':
    objects = s3_objects()
    # Should print 'cron(25 * * * ? *)'
    print(objects.get_content('alvkshchkd'))

