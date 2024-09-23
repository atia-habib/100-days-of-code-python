import auction_art 
print(auction_art.logo)

def find_highest_bidder(bidding_dictionary):

    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f" The winner is {winner} with the highest bid of ${highest_bid}")

bids = {}
continue_bidding = True
while continue_bidding:
    name = input("Enter your name: ")
    price = int(input("Enter the bidding price: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if should_continue == 'no':
        continue_bidding = False
        find_highest_bidder(bids)

    elif should_continue == 'yes': 
        print("\n" * 50)   

