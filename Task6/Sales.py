import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().splitlines()
    customers = defaultdict(lambda: defaultdict(int))
    
    for line in data:
        if not line.strip():
            continue
        customer, item, quantity = line.split()
        customers[customer][item] += int(quantity)
    
    for customer in sorted(customers.keys()):
        print(f"{customer}:")
        for item in sorted(customers[customer].keys()):
            print(f"{item} {customers[customer][item]}")

if __name__ == "__main__":
    main()