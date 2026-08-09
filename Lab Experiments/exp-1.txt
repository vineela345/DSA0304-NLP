import re

text = "My phone number is 9876543210"

pattern = r"\d+"

match = re.match(pattern, text)

if match:
    print("Match found:", match.group())
else:
    print("No match at the beginning")

search = re.search(pattern, text)

if search:
    print("Search found:", search.group())
else:
    print("Pattern not found")
