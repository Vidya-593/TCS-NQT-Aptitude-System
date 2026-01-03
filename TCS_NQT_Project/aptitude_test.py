score = 0

print("Welcome to TCS NQT Aptitude Practice Test\n")

# Question 1
print("1. What is 20% of 150?")
print("A. 20")
print("B. 25")
print("C. 30")
print("D. 35")

ans = input("Enter your answer (A/B/C/D): ")

if ans.upper() == "C":
    score += 1

# Question 2
print("\n2. Simple Interest on ₹1000 at 10% per annum for 2 years is?")
print("A. 100")
print("B. 200")
print("C. 300")
print("D. 400")

ans = input("Enter your answer (A/B/C/D): ")

if ans.upper() == "B":
    score += 1

# Question 3
print("\n3. Average of 2, 4, 6, 8 is?")
print("A. 4")
print("B. 5")
print("C. 6")
print("D. 7")

ans = input("Enter your answer (A/B/C/D): ")

if ans.upper() == "B":
    score += 1

# Question 4
print("\n4. If CP = ₹50 and SP = ₹60, Profit = ?")
print("A. ₹5")
print("B. ₹8")
print("C. ₹10")
print("D. ₹12")

ans = input("Enter your answer (A/B/C/D): ")

if ans.upper() == "C":
    score += 1

# Question 5
print("\n5. 10 workers can complete work in 6 days. How many days for 5 workers?")
print("A. 10")
print("B. 12")
print("C. 8")
print("D. 15")

ans = input("Enter your answer (A/B/C/D): ")

if ans.upper() == "B":
    score += 1

print("\nTest Completed!")
print("Your Score:", score, "/ 5")