# Emergency Resource Dispatch Analyzer
# Personalization input:
birth = (input("Enter your birth year: "))
last_digit = int(birth[-1])
choice = last_digit % 3

n = int(input("Enter the number of resources requests: "))
requests = []

for i in range(n):
    v = int(input("Enter the request value: "))
    requests += [v]

# Creating different lists
low_demand = []
moderate_demand = []
high_demand = []
invalid_requests = []

total_valid = 0

# Classifying the requests
for request in requests:
    if request < 0:
        invalid_requests += [request]
    elif request==0:
        pass
    elif request >= 1 and request <= 20:
        low_demand += [request]
        total_valid += 1
    elif request >= 21 and request <= 50:
        moderate_demand += [request]
        total_valid += 1
    elif request > 50 :
        high_demand += [request]
        total_valid += 1

# Counting before personalization
orginal_low = len(low_demand)
orginal_moderate = len(moderate_demand)
orginal_high = len(high_demand)
removed_requests = 0

# Personalization based on the last digit of birth year
if choice == 0:
    removed_requests = orginal_low
    low_demand = []
elif choice == 1:
    removed_requests = orginal_high
    high_demand= []
elif choice == 2:
    removed_requests = orginal_low + orginal_high
    low_demand = []
    high_demand = []

# Final output
print("Last Digit of birth year:", last_digit)
print("Personalization Choice:", choice)
if choice == 0:
    print("Applied Rule: Remove Low Demand ")
elif choice == 1:
    print("Applied Rule: Remove High Demand ")
elif choice == 2:
    print("Applied Rule: Keep Only Moderate Demand")

print("Total valid requests:", total_valid)
print("Invalid requests:", invalid_requests)
print("Removed requests due to personalization:", removed_requests)

print("Requests after personalization:")
print("Low demand:", low_demand)
print("Moderate demand:", moderate_demand)
print("High demand:", high_demand)