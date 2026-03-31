percentage = float(input("Enter 12th percentage: "))
maths = input("Did you study Mathematics? (yes/no): ")
entrance_score = int(input("Enter entrance exam score: "))

eligible = True

if percentage < 75:
    print("Not Eligible: Minimum 75% required")
    eligible = False

if maths.lower() != "yes":
    print("Not Eligible: Mathematics is required")
    eligible = False

if entrance_score < 80:
    print("Not Eligible: Entrance score must be at least 80")
    eligible = False

if eligible:
    print("✅ Eligible for Admission")