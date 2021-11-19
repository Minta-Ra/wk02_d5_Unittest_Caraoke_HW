class Guest:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet 


    def deduct_ticket_fee_from_wallet(self, ticket_fee):
        if self.wallet > ticket_fee.fee:
            self.wallet -= ticket_fee.fee
            return self.wallet
        else:
            return "Not enough money to buy a ticket"