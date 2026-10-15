SIZE = 10
hash_table = [None] * SIZE 
def hash_function(roll):
    return roll % SIZE
def insert(roll, name):
    key = hash_function(roll)
    original_key = key
    while hash_table[key] is not None and hash_table[key] != "DELETED":
        if hash_table[key]["roll"] == roll:
            print("Student with this Roll Number already exists!")
            return
        key = (key + 1) % SIZE
        if key == original_key:
            print("Hash Table is Full! Cannot insert.")
            return
    hash_table[key] = {"roll": roll, "name": name}
    print(f"Student {name} (Roll: {roll}) inserted successfully at index {key}")
def search(roll):
    key = hash_function(roll)
    original_key = key
    while hash_table[key] is not None:
        if hash_table[key] != "DELETED" and hash_table[key]["roll"] == roll:
            print(f"Student Found → Roll: {hash_table[key]['roll']}, Name: {hash_table[key]['name']}")
            return
        key = (key + 1) % SIZE
        if key == original_key:
            break
    print("Student not found!")

def delete(roll):
    key = hash_function(roll)
    original_key = key

    while hash_table[key] is not None:
        if hash_table[key] != "DELETED" and hash_table[key]["roll"] == roll:
            print(f"Deleted → Roll: {hash_table[key]['roll']}, Name: {hash_table[key]['name']}")
            hash_table[key] = "DELETED" 
            return
        key = (key + 1) % SIZE
        if key == original_key:
            break
    print("Student not found! Cannot delete.")

def display():
    print("\n----- HASH TABLE -----")
    print(f"{'Index':<8}{'Roll No':<12}{'Name'}")
    print("-" * 35)
    for i in range(SIZE):
        if hash_table[i] is None:
            print(f"{i:<8}{'Empty'}")
        elif hash_table[i] == "DELETED":
            print(f"{i:<8}{'DELETED'}")
        else:
            print(f"{i:<8}{hash_table[i]['roll']:<12}{hash_table[i]['name']}")
    print("-" * 35)

# ---------------- MENU DRIVEN PROGRAM ----------------
while True:
    print("\n===== STUDENT REGISTRATION SYSTEM (HASHING) =====")
    print("1. Insert a Student Record")
    print("2. Search for a Student by Roll Number")
    print("3. Delete a Student Record")
    print("4. Display the Hash Table")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        try:
            roll = int(input("Enter Roll Number: "))
            name = input("Enter Student Name: ")
            insert(roll, name)
        except ValueError:
            print("Invalid Roll Number! Please enter an integer.")

    elif choice == "2":
        try:
            roll = int(input("Enter Roll Number to search: "))
            search(roll)
        except ValueError:
            print("Invalid Roll Number!")

    elif choice == "3":
        try:
            roll = int(input("Enter Roll Number to delete: "))
            delete(roll)
        except ValueError:
            print("Invalid Roll Number!")

    elif choice == "4":
        display()

    elif choice == "5":
        print("Exiting program... Thank you!")
        break

    else:
        print("Invalid choice! Please enter 1-5.")
