def response(hey_bob):
    if hey_bob.rstrip().endswith('?'):
        return "Sure."
    elif hey_bob.isspace() or hey_bob is None:
        return "Fine. Be that way!"
    elif hey_bob == (hey_bob.upper()):
        return "Whoa, chill out!"
    else:
        return "Whatever."
