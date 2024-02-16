'''
Do not remove any text from these comments
5.	Questions next Modify the Python program for Question 4 to allow my_list
to store multiple data types of data. The data does NOT have to be sorted
in this case but is added to the list in the order that the user enters it.

my_list = []
Enter an integer data: 1
Enter a string: SUNWAY
Enter a string: UNIVERSITY
Enter a list data: [1.0, -1, 'A']
Enter a float data: 0.1
my_list = [1.0, 'SUNWAY', 'UNIVERSITY', [1.0, -1, 'A'], 0.1]
my_list = [1.0, 'SUNWAY', 'UNIVERSITY', [1.0, -1, 'A']]
my_list = [1.0, 'SUNWAY', 'UNIVERSITY']
my_list = [1.0, 'SUNWAY']
my_list = [1.0]
my_list = []

Function to use: float(), input(), print(), ast.literal_eval(), 
keyword: del
Operators: +, -, >=
Structure: while
'''

def main():
    count = 1
    while count <= 5:
        num = float(input("Enter a number: "))
        my_list.append(num)
        count = count + 1

    my_list.sort()
    print("my_list =" , my_list)

    lastindex = 4
    while lastindex >= 0:
        del my_list[lastindex]
        print("my_list =" , my_list)
        lastindex = lastindex - 1
    return 0


