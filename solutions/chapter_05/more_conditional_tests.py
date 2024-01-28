cars = ["toyota", "ford", "chevrolet", "honda", "volkswagen",
        "bmw", "mercedes-benz", "audi", "hyundai", "nissan"]
motorcycles = ["Honda", "Yamaha", "Harley-Davidson", "Ducati", "Kawasaki"]

print(f"Is the length of motorcycles equal to cars length? Prediction: False.")
print(len(cars) == len(motorcycles))
print(f"Is the length of motorcycles not equal to cars length? Prediction: True.")
print(len(cars) != len(motorcycles))
print(f"Is Honda in both cars and motorcycles? Prediction: True")
motorcycle_01 = motorcycles[0].lower()
car_04 = cars[3]
print(motorcycle_01 == car_04)
print(f"Is the length of the car 'volkswagen' between 9 and 11 characters? Prediction: True.")
car_05 = len(cars[4])
print(9 <= car_05 <= 11)  # and
print(f"\nIs the length of the car 'ford' between 9 and 11 characters? Prediction: False.")
car_02 = len(cars[1])
print(9 <= car_02 <= 11)  # and
print(f"\nIs honda in cars list? Prediction: True.")
print('honda' in cars)
print(f"\nIs subaru in cars list? Prediction: False.")
print('subaru' in cars)
print(f"\nIs subaru and nissan in cars list? Prediction: False.")
print('subaru' in cars and 'nissan' in cars)
print(f"\nIs audi and nissan in cars list? Prediction: True.")
print('audi' in cars and 'nissan' in cars)
print(f"\nIs audi not in cars list? Prediction: False.")
print('audi' not in cars)
