# Temperature Classifier: Freezing, Very Cold, Cold, Moderate, Hot, Very Hot

temp = int(input("\nInput the temperature: "))

if temp <= 0:
    print("\nIt's Freezing.")
elif temp <= 10:
    print("\nIt's Very Cold.")
elif temp <= 20:
    print("\nIt's Cold.")
elif temp <= 30:
    print("\nIt's Moderate.")
elif temp <= 40:
    print("\nIt's Hot.")
else:
    print("\nIt's Very Hot.")
