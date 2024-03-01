#unpacking:

def total(pound, note, doller):
    return (pound *17 + note) * 29 + doller

coins = [100,50, 25]

print(total(coins[0], coins[1], coins[2]), "nuts")