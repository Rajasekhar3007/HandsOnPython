import copy

def create_inventory():
    inventory = [
        {
            "item": "Laptop",
            "details": {"price": 50000, "stock": 10},
            "supplier": {"name": "ABC", "rating": 4.5}
        },
        {
            "item": "Phone",
            "details": {"price": 20000, "stock": 25},
            "supplier": {"name": "XYZ", "rating": 4.2}
        },
        {
            "item":"Television",
            "details": {"price": 30000, "stock": 45},
            "supplier": {"name": "Samsung", "rating": 4.8}
        },
        {
            "item": "Air Conditioner",
            "details": {"price": 60000, "stock": 50},
            "supplier": {"name": "Aquarium", "rating": 4.9}
        },
        {
            "item": "Battery",
            "details": {"price": 70000, "stock": 100},
            "supplier": {"name": "Bosch", "rating": 4.9}
        }
    ]
    return inventory


def apply_changes(data, roll):
    index = roll % len(data)
    print("Index value:", index)

    choice = input("Enter stock operation (inc/dec): ")
    value = int(input("Enter value: "))

    for i in range(len(data)):
        if i == index:
            old_price = data[i]["details"]["price"]
            old_stock = data[i]["details"]["stock"]

            data[i]["details"]["price"] = int(old_price * 0.9)

            if choice == "inc":
                data[i]["details"]["stock"] += value
                action = "increased"
            else:
                data[i]["details"]["stock"] -= value
                action = "decreased"

            return {
                "item": data[i]["item"],
                "index": index,
                "old_price": old_price,
                "new_price": data[i]["details"]["price"],
                "old_stock": old_stock,
                "new_stock": data[i]["details"]["stock"],
                "action": action,
                "value": value
            }


def compare_data(original, other):
    changed = 0
    same = 0

    for i in range(len(original)):
        if original[i] == other[i]:
            same += 1
        else:
            changed += 1

    return (changed, same)

original = create_inventory()
original_backup = copy.deepcopy(original)

roll = int(input("Enter roll number: "))

shallow = copy.copy(original)
deep = copy.deepcopy(original)

print("\n BEFORE CHANGES ")
print("Original:", original)
print("Shallow :", shallow)
print("Deep    :", deep)

print("\n SHALLOW COPY ")
mod1 = apply_changes(shallow, roll)

print("\nAfter shallow change:")
print("Original:", original)
print("Shallow :", shallow)

print("\n DEEP COPY ")
mod2 = apply_changes(deep, roll)

print("\nAfter deep change:")
print("Original:", original)
print("Deep    :", deep)

print("\n FINAL OUTPUT ")
print("Original:", original)
print("Shallow :", shallow)
print("Deep    :", deep)

res1 = compare_data(original_backup, shallow)
res2 = compare_data(original_backup, deep)

print("\n DIFFERENCES ")
print("Original vs Shallow:", res1)
print("Original vs Deep   :", res2)

print("\n TUPLE SUMMARY ")
print("Shallow (changed, same):", res1)
print("Deep    (changed, same):", res2)

print("\n MODIFICATIONS ")
print("Shallow ->", mod1["item"], "Price:", mod1["old_price"], "to", mod1["new_price"])
print("Stock:", mod1["old_stock"], "to", mod1["new_stock"])

print("Deep ->", mod2["item"], "Price:", mod2["old_price"], "to", mod2["new_price"])
print("Stock:", mod2["old_stock"], "to", mod2["new_stock"])

print("\n ANALYSIS ")
print("Shallow copy changed original because inner data is shared.")
print("Deep copy did not change original because it is separate.")
print("Example: change in shallow affected original, but deep did not.")