import boto3

expected_sizes = [
    60,
    80,
    120,
    180,
    192,
    200,
    230,
    300,
    600,
    640,
    750,
    1000,
    1242,
    1500,
]

s3local = boto3.session.Session(profile_name='s3local')
s3 = s3local.resource('s3', endpoint_url='http://localhost:4569', aws_access_key_id='S3RVER', aws_secret_access_key='S3RVER')
bucket = s3.Bucket('sfb-legal-music-smapi')
for size in expected_sizes:
    assert 'd/albumarts/test_{}.png'.format(size) in bucket_objects, '{} should be in bucket'.format(size)

bucket.objects.delete()

# Upload to S3
with open('test.png', 'rb') as data:
    s3.meta.client.upload_fileobj(data, 'sfb-legal-music-bucket9-int', 'albumarts/test.png')

# Get resized images and append to list
bucket_objects = []
for obj in bucket.objects.all():
    bucket_objects.append(obj.key)