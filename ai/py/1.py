location = input("Enter initial location (A/B): ").upper()

A = input("Enter status of Room A (Dirty/Clean): ").capitalize()
B = input("Enter status of Room B (Dirty/Clean): ").capitalize()

while A == "Dirty" or B == "Dirty":
    if location == "A":
        if A == "Dirty":
            print("Room A is Dirty.")
            print("Action: SUCK")
            A = "Clean"
        else:
            print("Room A is Clean.")
            print("Action: Move Right to Room B")
            location = "B"
    else:
        if B == "Dirty":
            print("Room B is Dirty.")
            print("Action: SUCK")
            B = "Clean"
        else:
            print("Room B is Clean.")
            print("Action: Move Left to Room A")
            location = "A"

print("\nBoth rooms are clean.")
print("Action: No Operation (NoOp)")
