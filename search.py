
import json
import os

FILE = "items.json"


def load_items():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []


def save_items(items):
    with open(FILE, "w") as f:
        json.dump(items, f, indent=4)


def add_item(items):
    print("\n1. Lost Item")
    print("2. Found Item")

    choice = input("Choose type: ")

    if choice not in ["1", "2"]:
        print("Invalid choice!")
        return

    name = input("Enter item name: ")
    location = input("Enter location: ")
    description = input("Enter description: ")

    item = {
        "id": len(items) + 1,
        "type": "Lost" if choice == "1" else "Found",
        "name": name,
        "location": location,
        "description": description
    }

    items.append(item)
    save_items(items)

    print("\nReport submitted successfully!")


def view_items(items):
    print("\n===== ALL REPORTS =====")

    if not items:
        print("No reports available.")
        return

    for item in items:
        print("\nID:", item["id"])
        print("Type:", item["type"])
        print("Name:", item["name"])
        print("Location:", item["location"])
        print("Description:", item["description"])


def search_item(items):
    keyword = input(
        "\nEnter item name or location to search: "
    ).lower()

    results = [
        item for item in items
        if keyword in item["name"].lower()
        or keyword in item["location"].lower()
    ]

    if results:
        print("\n===== SEARCH RESULTS =====")
        for item in results:
            print(
                f"{item['type']} | {item['name']} | "
                f"{item['location']}"
            )
    else:
        print("No matching items found.")


def find_matches(items):
    print("\n===== POSSIBLE MATCHES =====")

    lost_items = [
        x for x in items if x["type"] == "Lost"
    ]

    found_items = [
        x for x in items if x["type"] == "Found"
    ]

    matches = 0

    for lost in lost_items:
        for found in found_items:

            name_match = (
                lost["name"].lower() == found["name"].lower()
            )

            location_match = (
                lost["location"].lower()
                == found["location"].lower()
            )

            if name_match or location_match:
                matches += 1
                print("\nPossible match!")
                print("Lost:", lost["name"])
                print("Found:", found["name"])
                print("Lost location:", lost["location"])
                print("Found location:", found["location"])

    if matches == 0:
        print("No possible matches found.")


def main():
    items = load_items()

    while True:
        print("\n===== LOST & FOUND SYSTEM =====")
        print("1. Report an item")
        print("2. View all reports")
        print("3. Search items")
        print("4. Find possible matches")
        print("5. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            add_item(items)

        elif choice == "2":
            view_items(items)

        elif choice == "3":
            search_item(items)

        elif choice == "4":
            find_matches(items)

        elif choice == "5":
            print("Thank you!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
