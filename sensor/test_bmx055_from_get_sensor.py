import get_sensor

value = get_sensor.accl()

accl_x = value[0]

if value[2]>1000:
    print("drop!")
else:
    print("flying")

print(value)
print(accl_x)
print(get_sensor.accl()[0])
