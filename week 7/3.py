def countries():
    print("Enter country's name and know its capital")
    print("Type exit to exit the program")
    countries={}
        
    while True:
        country=input("Enter the country name: ").lower()

        if country=="exit":
            print("Exiting the program")
            for country,capital in countries.items():
                print(f"{country.title()}:{capital.title()}")
            break
        
        else:
            capital=input(f"Please enter the capital's name of {country.title()}.I don't know it yet!: ")
            countries[country]=capital
            print(f"The capital of {country.title()} is {capital.title()}") 

countries()     