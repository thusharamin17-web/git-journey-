def response(hey_bob):
    # Clean up whitespace from the front and back of the string
    hey_bob = hey_bob.strip()

    # Check for silence (empty string after trimming whitespace)
    if not hey_bob:
        return "Fine. Be that way!"

    # Check conditions
    is_question = hey_bob.endswith("?")
    is_yelling = hey_bob.isupper()

    # Determine Bob's response based on the rules
    if is_question and is_yelling:
        return "Calm down, I know what I'm doing!"
    elif is_question:
        return "Sure."
    elif is_yelling:
        return "Whoa, chill out!"
    else:
        return "Whatever."
