## task 1

# total = 100
 
# while total > 0:
#     try:
#         n = int(input("Enter some number: "))
#         if (total - n < 0):
#             print("Be careful - you can't use more than you have! Try again.")
#             n = int(input("Enter some number: "))
#         total = total - n
#         print("Now you resorce is", total)
#     except ValueError:
#         print("You entered not a number! Try again.")
 
# print("Resource exhausted!")


## task 2

i = 0

while i <= 20:
    print("2**%d =" % i, 2**i)
    i+=1