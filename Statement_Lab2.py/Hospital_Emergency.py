age = int(input("Enter patient age: "))
heart_rate_abnormal = input("Is heart rate abnormal? (yes/no): ")
severe_injury = input("Is there severe injury? (yes/no): ")

if heart_rate_abnormal.lower() == "yes" or severe_injury.lower() == "yes":
    category = "Critical"
else:
    category = "Moderate"

# Upgrade condition
if age > 65 and category == "Moderate":
    category = "Critical"

print("Patient Category:", category)