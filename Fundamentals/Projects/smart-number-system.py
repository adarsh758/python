# Run the Program infinite time
while True:
    # Show Menu
    print("""===== Menu =====
                1. Range Analyzer
                2. Print Number Pattern
                3. Single Number Check
                4. EXIT
 """)
    # Take user input
    user_choice = int(input("Please select a option(1 to 4): "))

    # Ask for correct input untill the correct input
    while user_choice < 1 or user_choice > 4:
        user_choice = int(input("Please select a option(1 to 4): "))

    # ========= 1. Range Analyzer ==========
    if user_choice == 1:
        starting_num = int(input("Please enter the starting number (1 to 100): "))

        ending_number = int(input("Please enter the ending number (1 to 100): "))

        # Ask for correct starting number
        while starting_num <= 0:
            starting_num = int(input("Please select a correct starting number (1 to 100): "))

        # Ask for correct ending number
        while ending_number <= 0:
            ending_number = int(input("Please select a correct ending numnber (1 to 100): "))

        # skip the loop if number is greater than 100
        if starting_num > 100 or ending_number > 100:
            print("Number too large. Try again.")
            continue

        if starting_num > ending_number:
            starting_num, ending_number = ending_number, starting_num

        # 1. Check every number between start, and end
        for num in range(starting_num, ending_number + 1):
            print(f"{num}: ")
            # skip the loop if number is divisible by 7
            if  num % 7 == 0:
                print("\t skipped (divisible by 7)")
                continue

            # check for even/odd numbers and print output
            if num % 2 == 0: 
                print("\t is a even number")
            else:
                print("\t is a odd number")

            # check for prime numbers and print output
            if num <= 1: 
                is_prime = False
            else:
                is_prime=True
                for i in range(2, int(num**0.5)+1):
                    if num%i == 0:
                        is_prime = False
                        break
                if is_prime: print("\t is a prime number")
                if not is_prime: print("\t is not a prime number")

            # Check if num is divisible by 3 and 5
            divisible_by_3 = False
            divisible_by_5 = False
            if num%3 ==0:
                divisible_by_3 = True
            if num % 5 == 0:
                divisible_by_5 = True
                
            if divisible_by_3 and divisible_by_5:
                print("\t is divisible by 3 and 5")
            elif divisible_by_3:
                print("\t is divisible by 3")
            elif divisible_by_5:
                print("\t is divisible by 5")

        
    # ========== 2. Pattern Print ==========
    elif user_choice == 2:
        pattern_size=int(input("Please enter a number (1 to 10: )"))

         # if user entered a number not in between 1 to 10, ask user again
        while pattern_size <= 0 or pattern_size > 10:
            pattern_size=int(input("Please enter a number (1 to 10: )"))

        # Print pattern if pattern_size is between 1 to 10
        for i in range(pattern_size + 1):
            for j in range(i):
                print(j+1, end=" ")
            print()

        

    # ========= 3. Single Number Check ==========
    elif user_choice == 3:
        number = int(input("Please enter a number (1 to 100): "))

        # Ask for correct starting number
        while number <= 0:
            number = int(input("Please select a correct number (1 to 100): "))

        # End the program if number is greater than 100
        if number > 100:
            print("Number too large. Try again.")
            continue

        print(f"{number}: " )

        # check for even/odd numbers and print
        if number % 2 == 0 : 
            print("\t is a even number")
        else:
            print("\t is a odd number")

        # check for prime numbers and print
        if number <= 1: 
            is_prime = False
        else:
            is_prime=True
            for i in range(2, int(number**0.5)+1):
                if number%i == 0:
                    is_prime = False
                    break
            if is_prime: print("\t is a prime number")
            if not is_prime: print("\t is not a prime number")
        
        # Find factorial
        factorial=1
        for num in range(number, 0, -1):
            factorial *= num
        print(f"factorial: {factorial}")

    # ========== 4. Exit ==========
    elif user_choice == 4:
        break

            

        
            

        
    