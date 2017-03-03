class UnencryptableRecipients(Exception):
    def __init__(self, encrypting_identities, encrypting_recipients, plaintext_recipients):
        self.encrypting_identities = encrypting_identities
        self.encrypting_recipients = encrypting_recipients
        self.plaintext_recipients = plaintext_recipients
