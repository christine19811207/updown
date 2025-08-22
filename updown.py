def sockMerchant(n, ar):
    total = 0
    pairs = {}
    for sock in ar:
        if sock in pairs:
            pairs[sock] += 1
            if pairs[sock] %2 ==0:
                total += 1
            else:
                pairs[sock] = 1
    return total