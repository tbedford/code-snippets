import csv

def load_user_registrations(csv_file):
    registrations = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            registrations.append(row)
    return registrations

# Example usage
csv_file = "user_regs.csv"
user_registrations = load_user_registrations(csv_file)
for registration in user_registrations:
    print(registration)




