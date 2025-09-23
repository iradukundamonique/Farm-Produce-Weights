# ------------------------------
# Farm Produce Weights Program
# ------------------------------

from array import array

# ------------------------------
# Integers: Farm Produce Weights
# ------------------------------

print("\n -------------Integers and Short report -----------------\n")
produce_weights = [25, 30, 18, 22, 40, 35]  # Example weights in kilograms

total_weight = sum(produce_weights)
average_weight = total_weight / len(produce_weights)
min_weight = min(produce_weights)
max_weight = max(produce_weights)

# ------------------------------
# Strings: Formatted f-string Report
# ------------------------------
report = (
    f"Farm Produce Weights Report\n"
    f"Total weight of produce: {total_weight} kg\n"
    f"Average weight: {average_weight:.2f} kg\n"
    f"Minimum weight: {min_weight} kg, Maximum weight: {max_weight} kg\n"
)
print(report)

print("\n -------------Check status with Boolean -----------------\n")
# ------------------------------
# Booleans: Apply Threshold Condition
# ------------------------------
threshold = 28
if average_weight > threshold and max_weight > 35:  # compound condition
    print("Status: Above Standard\n")
else:
    print("Status: Below Standard\n")

# ------------------------------
# Lists: Maintain and Modify Records
# ------------------------------

print("\n -------------List (Adding, removing and sorting) -----------------\n")
print("Original list of weights:", produce_weights)

# Add a new element
produce_weights.append(27)

# Remove elements less than 20 (condition-based removal)
produce_weights = [w for w in produce_weights if w >= 20]

# Sort the list
produce_weights.sort()

print("Modified and sorted list of weights:", produce_weights, "\n")

# ------------------------------
# Arrays: Store Fixed-Size Subset
# ------------------------------

print("\n -------------Array (Comparing) -----------------\n")
subset_array = array('i', produce_weights[:4])  # first 4 weights
array_sum = sum(subset_array)
list_sum = sum(produce_weights)

print("Array subset:", subset_array.tolist())
print("Sum of array subset:", array_sum)
print("Sum of full list:", list_sum)

if array_sum < list_sum:
    print("Array subset sum is smaller than list sum.\n")

# ------------------------------
# Dictionaries: Records of Produce
# ------------------------------

print("\n -------------Dictionaries ------------\n")
produce_records = [
    {"id": 1, "name": "Tomatoes", "value": 25},
    {"id": 2, "name": "Potatoes", "value": 30},
    {"id": 3, "name": "Carrots", "value": 18},
]

# Update one record (Carrots value changed)
produce_records[2]["value"] = 20

# Delete one record (remove Potatoes)
produce_records = [record for record in produce_records if record["id"] != 2]

# Compute total of 'value'
total_values = sum(record["value"] for record in produce_records)

print("Updated Produce Records:")
for record in produce_records:
    print(record)

print(f"\nTotal value of produce records: {total_values} kg")
