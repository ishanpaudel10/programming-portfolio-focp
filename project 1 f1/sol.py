import sys 
def read_from_file(filename):
    try:
        with open(filename,'r') as f:
            return f.readlines()
    except FileNotFoundError:
        print("The filename you entered is not there. Please enter correct filename")


def main():
    if len(sys.argv)<2:
        print("Enter the filename properly in command line")
        sys.exit(1)
        
    file=sys.argv[1]
    lines=read_from_file(file)

    if lines==None:
        exit(0)

    location_of_race=lines[0].strip()
    print(f"Location of the race is {location_of_race}")

    highest_time=float('inf')
    fastest_driver=" "

    for line in lines[1:]:
        three_letter_code=line[:3]
        lap_time=float(line[3:])

        if lap_time<highest_time:
            highest_time=float(lap_time)
            fastest_driver=three_letter_code
        
    print(f"{fastest_driver} with a time of {highest_time} seconds is the fastest driver")


main()