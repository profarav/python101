person = {"first_name": "John", "gender": "male", "address": "asdasd", "phone": "4699234321"}
stalker = input("what do you want to know about the person:").lower()
result = person.get(stalker, "sorry that information isnt available")
print(result)
