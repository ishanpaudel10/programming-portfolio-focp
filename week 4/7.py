#7.
import statistics
def val():
    temp1=float(input("Enter the first temperature: "))
    temp2=float(input("Enter the second temperature: "))
    temp3=float(input("Enter the third temperature: "))
    temp4=float(input("Enter the fourth temperature: "))
    temp5=float(input("Enter the fifth temperature: "))
    temp6=float(input("Enter the sixth temperature: "))
    return temp1,temp2,temp3,temp4,temp5,temp6

def compare(temp1,temp2,temp3,temp4,temp5,temp6):
    temperatures=[temp1,temp2,temp3,temp4,temp5,temp6]
    print(f'The minimum temperature is: {min(temp1,temp2,temp3,temp4,temp5,temp6)}')
    print(f'The maximum temperature is: {max(temp1,temp2,temp3,temp4,temp5,temp6)}')
    print(f'The mean of temperature is: {statistics.mean(temperatures)}')

temp1,temp2,temp3,temp4,temp5,temp6=val()
d=compare(temp1,temp2,temp3,temp4,temp5,temp6)
