import datetime
import time
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature, BadData

from StudentManageSys.settings import SECURE_KEY

s = Serializer(secret_key=SECURE_KEY['SECRET_KEY'], salt=SECURE_KEY['AUTH_SALT'],
               expires_in=60 * 60 * 7)
timestamp = time.time()
data = {'user_id': '789456123', 'iat': timestamp}
print(data)
token = s.dumps(data)
print(token)

s = Serializer(secret_key=SECURE_KEY['SECRET_KEY'], salt=SECURE_KEY['AUTH_SALT'])
try:
    data = s.loads(token)
except SignatureExpired:
    msg = 'token expired'
    print(msg)
except BadSignature as e:
    encoded_payload = e.payload
    if encoded_payload is not None:
        try:
            s.load_payload(encoded_payload)
        except BadData:
            msg = 'token tampered'
            print(msg)
    msg = 'badSignature of token'
    print(msg)
except:
    msg = 'wrong token with unknown reason'
    print(msg)

print(data)
if 'user_id' not in data:
    msg = 'illegal payload inside'
    print(msg)
msg = 'user(' + data['user_id'] + ') logged in by token.'
userId = data['user_id']
