import time
import json
import random
import hmac
import base64
secret_key = b'ajflasjflasjlf'


def basic_salt():
    return [chr(i) for i in range(97, 122)] + [chr(i) for i in range(65, 90)]


def generate_token(payload: dict = {}):
    payload_byte = json.dumps({
        'expire': time.time() + (payload.get('expire') if
                                 payload.get('expire') else 3600),
        'salt': payload.get('salt') if payload.get('salt') else
        ''.join(random.sample(basic_salt(), 8))
    }).encode('utf-8')
    sign = hmac.new(secret_key, payload_byte).digest()
    token = base64.encodebytes(payload_byte + sign)
    return token.decode('utf-8').replace('\n', '')


def token_expired(token):
    payload_byte = base64.decodebytes(token.encode('utf-8'))[:-16]
    payload = json.loads(payload_byte)
    return True if payload.get('expire') < time.time() else False


token = generate_token({'expire': 0.11})
print(token)
print(token_expired(token))
