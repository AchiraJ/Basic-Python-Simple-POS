# ONE-P Store Sale

fixed_Price = 19.99
old_books_discount= 50/100
fancy_books_discount = 30/100
yummy_books_discount = 20/100

# Get the user input for different categories of books

num_Books_Old = int(input("\nHow many Old Books do you want? "))
num_Books_Fancy = int(input("\nHow many Fancy Books do you want? "))
num_Books_Yummy = int(input("\nHow many Yummy Books do you want? "))

# cost of each category of books after discount
Discounted_Old_Books= fixed_Price * old_books_discount
Discounted_Fancy_Books = fixed_Price * fancy_books_discount
Discounted_Yummy_Books = fixed_Price * yummy_books_discount

# Total cost per category for the customer
Total_cost_old_books = num_Books_Old * Discounted_Old_Books
Total_cost_fancy_books = num_Books_Fancy * Discounted_Fancy_Books
Total_cost_Yummy_books = num_Books_Yummy * Discounted_Yummy_Books

# print total cost for the specific order
Total = Total_cost_fancy_books + Total_cost_old_books +Total_cost_Yummy_books

print(f"\n The total cost is ${Total}. \n\n Thanks for shopping with us and welcome again!!!! \n")