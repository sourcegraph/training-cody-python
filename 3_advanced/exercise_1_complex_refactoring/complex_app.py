
def process_orders(orders):
    total_cost = 0
    for order in orders:
        cost = 0
        if order['type'] == 'A':
            cost = order['quantity'] * 100
        elif order['type'] == 'B':
            cost = order['quantity'] * 200
        total_cost += cost
    print(f"Total cost: ${total_cost}")
    return total_cost

def generate_report(orders):
    report = "Order Report\n"
    for order in orders:
        report += f"Order Type: {order['type']}, Quantity: {order['quantity']}\n"
    report += f"Total Cost: {process_orders(orders)}"
    return report

def main():
    orders = [
        {'type': 'A', 'quantity': 2},
        {'type': 'B', 'quantity': 3},
        {'type': 'A', 'quantity': 1},
    ]
    print(generate_report(orders))

if __name__ == "__main__":
    main()