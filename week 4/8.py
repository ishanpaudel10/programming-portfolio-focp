#8.
import statistics
def temp():
    temps=[]
    while True:
        temp=(input("Enter the temperature (press enter to exit): "))
        if temp=="":
            break
        else:
            temps.append(float(temp))
    return temps

def display(temps):
    print(f"The minimum temperature is:{min(temps)}")
    print(f"The maximum temperature is:{max(temps)}")
    print(f"The mean temperature is:{statistics.mean(temps)}")

temps=temp()
display(temps)