import uuid
for i in range (30):
    ram=uuid.uuid4().hex[:15]
print("The random password generated is:",ram)
