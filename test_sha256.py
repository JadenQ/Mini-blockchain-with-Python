# import sha256
from hashlib import sha256
# text to hash
text = 'I am excited to learn about blockchain!'

# print result
hash_result = sha256(text.encode())
hash_result = hash_result.hexdigest()
print(hash_result)
