import sys
import statistics

while True:
    t=(sys.argv[1:])

    if len(t)!=0:
        temp=[float(i) for i in t]
        temp_min=min(temp)
        temp_max=max(temp)
        temp_mean=statistics.mean(temp)

        print(f"Minimum temperature is:{temp_min}")
        print(f"Maximum temperature is:{temp_max}")
        print(f"Mean of temperatures is:{temp_mean}")
        break
    else:
        print('Please enter appropriate values')
        sys.exit()
