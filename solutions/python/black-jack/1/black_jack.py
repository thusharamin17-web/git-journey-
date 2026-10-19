"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    Parameters:
        card (str): The given card.

    Returns:
        int: The value of a given card.
    """
    face = ('J', 'Q', 'K')
    if card == 'A':
        return 1
    elif card in face:
        return 10
    else:
        return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand."""
    val_one = value_of_card(card_one)
    val_two = value_of_card(card_two)
    if val_one > val_two:
        return card_one
    elif val_two > val_one:
        return card_two
    else:
        return card_one, card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card."""
    # In hand, an Ace counts as 11 according to the problem docstring
    val_one = 11 if card_one == 'A' else value_of_card(card_one)
    val_two = 11 if card_two == 'A' else value_of_card(card_two)
    
    hand_value = val_one + val_two
    if card_one == 'A' or card_two == 'A' or hand_value + 11 > 21:
        return 1
    return 11


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'."""
    face_cards = ('10', 'J', 'Q', 'K')
    return (card_one == 'A' and card_two in face_cards) or (card_two == 'A' and card_one in face_cards)


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands."""
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet."""
    hand_total = value_of_card(card_one) + value_of_card(card_two)
    return hand_total in (9, 10, 11)
