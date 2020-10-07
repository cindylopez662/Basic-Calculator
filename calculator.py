#functions, baby
'''
simple calculator
to practice functions and ifs 
'''
#choose subtraction, addition, x, or /
#get commands for adding, subtracting, multiplying, and dividing in a loop in the main function - indented
def adding(num1, num2):
    sum = num1 + num2
    return sum 
def subtract(num1, num2):
    difference = num1 - num2
    return difference
def multiply(num1, num2):
    product = num1 * num2
    return product
def divide(num1, num2):
    quotient = num1 / num2
    return quotient

#to do: verify that u entered a number, optimize the num conversion, (allow decimals?)

if __name__ == '__main__':
    questions = ['add', 'subtract', 'multiply', 'divide']
    while True:
            answer = input("Would you like to add, subtract, multiply, or divide? Press q to quit. ")
            if answer == 'q':
                print("Have a good day.")
                break
            if answer not in questions:
                print("That's not a valid answer.")
            num_answer = input("Which two numbers do you want to use? ").split(" ")

            if num_answer != int(num_answer[0], int(num_answer[1])):
                print("This is not a number")
            if num_answer != float(num_answer[0], float(num_answer[1])):
                print("This is not a number")
                
            if answer == 'add':
                add_answer = adding(int(num_answer[0]),int(num_answer[1]))
                print("You answer is", add_answer)
            if answer == 'subtract':
                sub_answer = subtract(int(num_answer[0]),int(num_answer[1]))
                print("Your answer is", sub_answer)
            if answer == 'multiply':
                mul_answer = multiply(int(num_answer[0]), int(num_answer[1]))
                print("Your answer is", mul_answer)
            if answer == 'divide':
                div_answer = divide(int(num_answer[0]), int(num_answer[1]))
                print("Your answer is", div_answer)    