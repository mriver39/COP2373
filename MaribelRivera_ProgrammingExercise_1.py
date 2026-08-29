# Cinema Ticket Pre-Sale Program
# Max 20 tickets total, max 4 per buyer

MAX_TICKETS = 20

def get_ticket_request():
    """Ask the user how many tickets they want and return the number."""
    return int(input("How many tickets would you like to buy (1–4)? "))

def process_sale(request, remaining):
    """Process the sale and return updated remaining tickets."""
    return remaining - request


def main():
    remaining = MAX_TICKETS
    buyers = 0

    print("Welcome to the Cinema Ticket Pre-Sale!")
    print("A maximum of 20 tickets are available.")
    print("Each buyer may purchase up to 4 tickets.\n")

    while remaining > 0:
        print(f"Tickets remaining: {remaining}")

        request = get_ticket_request()

        # Validate request
        if request < 1 or request > 4:
            print("Invalid amount. You may buy between 1 and 4 tickets.\n")
            continue

        if request > remaining:
            print(f"Only {remaining} tickets left. Please enter a smaller amount.\n")
            continue

        # Process sale
        remaining = process_sale(request, remaining)
        buyers += 1

        print(f"Purchase successful! Tickets remaining: {remaining}\n")

    print("All tickets have been sold!")
    print(f"Total number of buyers: {buyers}")


# Run the program
main()
