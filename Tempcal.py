def temperature_calculator():
    print("Temperature Calculator")
    print("------------------------")

    # Default temperature unit is Celsius
    temperature_unit = "Celsius"

    while True:
        print(f"\nCurrent temperature unit: {temperature_unit}")
        print("1. Convert temperature")
        print("2. Change temperature unit")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            temperature = float(input("Enter temperature value: "))

            if temperature_unit == "Celsius":
                print(f"{temperature}°C is equal to:")
                print(f"{temperature}°C = {temperature * 9/5 + 32}°F (Fahrenheit)")
                print(f"{temperature}°C = {temperature + 273.15}K (Kelvin)")

            elif temperature_unit == "Fahrenheit":
                print(f"{temperature}°F is equal to:")
                print(f"{temperature}°F = {(temperature - 32) * 5/9}°C (Celsius)")
                print(f"{temperature}°F = {(temperature - 32) * 5/9 + 273.15}K (Kelvin)")

            elif temperature_unit == "Kelvin":
                print(f"{temperature}K is equal to:")
                print(f"{temperature}K = {temperature - 273.15}°C (Celsius)")
                print(f"{temperature}K = {(temperature - 273.15) * 9/5 + 32}°F (Fahrenheit)")

        elif choice == "2":
            print("Select a new temperature unit:")
            print("1. Celsius")
            print("2. Fahrenheit")
            print("3. Kelvin")

            unit_choice = input("Enter your choice (1/2/3): ")

            if unit_choice == "1":
                temperature_unit = "Celsius"
            elif unit_choice == "2":
                temperature_unit = "Fahrenheit"
            elif unit_choice == "3":
                temperature_unit = "Kelvin"
            else:
                print("Invalid choice. Please try again.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

temperature_calculator()
