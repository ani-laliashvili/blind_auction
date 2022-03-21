from art import logo

def get_bids():
    bids, other_bidders = {}, 'yes'
    while other_bidders == 'yes':
        bidder_name = input("What is your name? ")
        bid = int(input("What's your bid?: $"))
        bids[bidder_name] = bid
        other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")
        print('\n' * 40)
    return bids

def find_highest_bidder(bids):
    highest_bid, winner = -1, ''
    for bidder in bids:
        if bids[bidder] > highest_bid:
            highest_bid = bids[bidder]
            winner = bidder
    return winner, highest_bid

if __name__ == "__main__":
    print(logo)
    print("Welcome to the secret auction program.")
    bids = get_bids()
    winner, highest_bid = find_highest_bidder(bids)
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

