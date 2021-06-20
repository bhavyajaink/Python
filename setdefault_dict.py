car = {"brand": "Ford",
       "model": "Mustang",
       "year": 1964}
print(car.setdefault("Bronco",'mod'))
print(car.setdefault("model"))
print(car)
