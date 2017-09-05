# edit the URI below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)

import boto3
from base64 import b64decode

pw_encrypted = "AQICAHjtJ2LwO2/txZD+zYoGbFjgst2ppIoQMVmgkCF0iTNoNQECoe4yuQRk1965HyebnvbVAAAAajBoBgkqhkiG9w0BBwagWzBZAgEAMFQGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMc+ZchgqDOWRXISiBAgEQgCfqmzjnA3MSqx4/cDMzlBx+x6shkXrmWQqOBOITer2RILypJHIpkV0="
user_encrypted = "AQICAHjtJ2LwO2/txZD+zYoGbFjgst2ppIoQMVmgkCF0iTNoNQFgMnILb/mIi8NPVGOp/rkoAAAAYzBhBgkqhkiG9w0BBwagVDBSAgEAME0GCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMjPPBaPFo+O2ZreKoAgEQgCCyw+rn4ZzJCvBhRG2/24/gXsKwx9OUBl3d72jrhrWZNA=="

client = boto3.client('kms')

pw = client.decrypt(CiphertextBlob=b64decode(pw_encrypted))['Plaintext']
user = client.decrypt(CiphertextBlob=b64decode(user_encrypted))['Plaintext']

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@piggy-dev-db.ckfc6vkfhmmc.us-east-2.rds.amazonaws.com:3306/piggydb'.format(user=user, password=pw)

# Uncomment the line below if you want to work with a local DB
#SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True
SECRET_KEY = 'dsaf0897sfdg45sfdgfdsaqzdf98sdf0a'
