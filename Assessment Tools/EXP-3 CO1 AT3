import re

text = input("Enter text: ")

while True:
    print("\n1. Search Date")
    print("2. Search Phone Number")
    print("3. Search Hashtag")
    print("4. Search Mention")
    print("5. Search Prefix")
    print("6. Search Suffix")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        pattern = r'\b\d{2}/\d{2}/\d{4}\b'
        result = re.findall(pattern, text)

    elif choice == "2":
        pattern = r'\b[6-9]\d{9}\b'
        result = re.findall(pattern, text)

    elif choice == "3":
        pattern = r'#\w+'
        result = re.findall(pattern, text)

    elif choice == "4":
        pattern = r'@\w+'
        result = re.findall(pattern, text)

    elif choice == "5":
        prefix = input("Enter prefix: ")
        pattern = r'\b' + re.escape(prefix) + r'\w*'
        result = re.findall(pattern, text, re.IGNORECASE)

    elif choice == "6":
        suffix = input("Enter suffix: ")
        pattern = r'\b\w*' + re.escape(suffix) + r'\b'
        result = re.findall(pattern, text, re.IGNORECASE)

    elif choice == "7":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
        continue

    if result:
        print("Matching Patterns:")
        for item in result:
            print(item)
    else:
        print("No matching pattern found.")
