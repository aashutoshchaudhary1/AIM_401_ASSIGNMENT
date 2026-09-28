#Task 1
name = input("Enter your Name: ")
total_spent = 0

#Task 2
for day in range(1, 4):
    spent = float(input("Enter money spent today ($): "))
    total_spent = total_spent + spent
    if spent > 20:
        print("Over your $20 budget today!")
    else:
        print("Great! Under budget today.")


#Task3
print("Total money spent over 3 days: $" + str(total_spent))
if total_spent <= 60:
    print("Overall Result: You stayed under your $60 total budget!")
else:
    print("Overall Result: You went over your $60 total budget!")
