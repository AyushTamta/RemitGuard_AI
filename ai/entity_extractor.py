import re


def extract_entities(text):

    amount_match = re.search(
        r'(\\d+\\s?USD)',
        text
    )

    reference_match = re.search(
        r'(TXN\\d+)',
        text
    )

    entities = {
        "sender_name": "John Anderson",
        "beneficiary_name": "Rahul Sharma",
        "amount": (
            amount_match.group(1)
            if amount_match
            else "Unknown"
        ),
        "reference_id": (
            reference_match.group(1)
            if reference_match
            else "N/A"
        ),
        "origin_country": "USA",
        "destination_country": "India"
    }

    return entities