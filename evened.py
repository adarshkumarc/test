number=int(input("enter the number:"))
if(number%2)==0:
    print("even number")
else:
    print("odd number")
#tempreture humidity
temperature = "Cold"
humidity = "Humid"

if temperature == "Cold":
    if humidity == "Dry":
        print("It's cold and dry.")
    elif humidity == "Humid":
        print("It's cold and humid.")
    else:
        print("Invalid humidity value.")
elif temperature == "Warm":
    if humidity == "Dry":
        print("It's warm and dry.")
    elif humidity == "Humid":
        print("It's warm and humid.")
    else:
        print("Invalid humidity value.")
else:
    print("Invalid temperature value.")
