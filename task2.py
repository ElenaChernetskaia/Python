time = int(input("Введите время в секундах >>> "))
hours = time // 3600
minutes = (time - 3600 * hours) // 60
seconds = time - 3600 * hours - 60 * minutes
print("Время в формате чч:мм:сс составляет", '%02i:%02i:%02i' % (hours, minutes, seconds))
