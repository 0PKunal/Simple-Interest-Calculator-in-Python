# A program to calculate simple interest(I)

#Input from user
P = float(input("Enter the principal amount(P): "))
r = float(input("Enter the rate of interest(r in %): "))
t = float(input("Enter the time(t in years): "))

#Calculate the interest
I = (P * r * t) / 100

#Show the calculation
print(f"\nSimple Interest(I) = {I:.2f}")

