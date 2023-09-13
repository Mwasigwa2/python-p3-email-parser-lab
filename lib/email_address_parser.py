import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        # Split the email addresses using a regular expression
        addresses = re.split(r'[,\s]+', self.email_addresses)
        # Remove empty strings and duplicate email addresses
        unique_addresses = list(set(filter(lambda x: x != '', addresses)))
        # Sort the addresses alphabetically
        unique_addresses.sort()
        return unique_addresses
