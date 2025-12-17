from login import hash_password, validate_password

p = "s3cret"
h = hash_password(p)
print("hashed:", h)
print("validate returns:", validate_password(p, h))