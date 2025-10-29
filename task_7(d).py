def categorize_tickets(ticket_ids):
    adult_tickets = list(filter(lambda x: x % 2 == 0, ticket_ids))
    child_tickets = list(filter(lambda x: x % 2 != 0, ticket_ids))
    return adult_tickets, child_tickets

ticket_ids = [101, 202, 305, 410, 513, 620, 723, 830, 945, 1050]
adult_tickets, child_tickets = categorize_tickets(ticket_ids)
print("Adult Tickets:", adult_tickets)
print("Child Tickets:", child_tickets)
