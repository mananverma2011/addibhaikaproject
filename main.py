def perform_operation(operation, symbol):
    while True:
        try:
            num1 = int(input(f"Enter the first number for {operation}: "))
            num2 = int(input(f"Enter the second number for {operation}: "))
            result = eval(f"{num1} {symbol} {num2}")
            print(f"The result of {operation} is: {result}\n")
            break  # Exit the loop if inputs are valid
        except ValueError:
            print("Invalid input! Please enter numeric values.")

def square_and_cube():
    for operation, power in [("square", 2), ("cube", 3)]:
        while True:
            try:
                num = float(input(f"Enter the number to {operation}: "))
                print(f"The {operation} of the number is: {num ** power}\n")
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")

print("Let's improve your mathematics skills!!")
for op, sym in [("addition", "+"), ("subtraction", "-"), ("multiplication", "*"), ("division", "/")]:
    perform_operation(op, sym)

if input("Do you want to continue? (yes/no): ").strip().lower() != "yes":
    print("Bye! Bye!")
    quit()

print("\nLet's now start with squaring and cubing of numbers! It would be fun!")
square_and_cube()

print("\nLet's talk about games!")
games = input("Do you play games? Can you name them: ")
print(f"I also like to play {games}. Good choice!")

while True:
    try:
        age = float(input("\nCan I get your age? "))
        advice = "focus on your studies" if age < 18 else "focus on your career"
        print(f"You should {advice}. My advice!!\n")
        break
    except ValueError:
        print("Invalid input! Please enter a valid age.")

if input("Do you want any help with your homework? (yes/no): ").strip().lower() == "yes":
    print("\nYou can try these applications:")
    resources = [
        "https://www.khanacademy.org/math",
        "https://unstuckstudy.com/",
        "https://byjus.com/",
        "https://www.popai.pro/",
        "https://www.mathsisfun.com/",
        "https://brainly.in/",
        "https://www.youtube.com/"
    ]
    print("\n".join(resources))
    print("\nBEST ADVICE IS TO DIY!!")
else:
    print("Bye! Bye!")
