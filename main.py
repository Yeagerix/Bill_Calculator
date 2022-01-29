#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇


# Prints a Welcome Message
print("Welcome to the tip calculator")
# Gives Input to the total bill
bill = float(input("What was the total bill? $"))
# Gives input to how much tip the person wants to give
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
# Gives input to person on how many people will split the bill
people = int(input("How many people to split the bill? "))

# Divides the tip percentage by 100 
tip_as_percent = tip / 100
print(tip_as_percent)
# multiplies the tip percentage by the bill 
total_tip_amount = bill * tip_as_percent
print(total_tip_amount)
# adds the result of the previous multiplication to the bill to gain the total bill amount
total_bill = bill + total_tip_amount


# divides the total bill by the amount of people spliting the bill
bill_per_person = total_bill / people
# creats a new variable called final_amount and stores the function (round) to the float bill_per_person to a 2 decimal point
final_amount = round(bill_per_person, 2)
# This next line is for formatting just to make sure that we always get two decimal points
final_amount = "{:.2f}".format(bill_per_person)
# Prints the final amount
print(f"Each person should pay: ${final_amount} ")

# the calucation is basically - (((12 / 100 = 0.12) 0.12 * 150 = 18.0) 150 + 18.0 = 178.0) / 5 = 33.60