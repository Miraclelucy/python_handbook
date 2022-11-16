# 1. Python Dictionary get() Method
# 1.1 return the value of an item that exist
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")

print(x)
# Mustang

# 1.2. Try to return the value of an item that do not exist
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("price", 15000)

print(x)
# 15000

# 1.3. dictionary.get(keyname, value)
# Parameter	Description
# keyname -	Required. The keyname of the item you want to return the value from
# value -	Optional. A value to return if the specified key does not exist. Default value None

