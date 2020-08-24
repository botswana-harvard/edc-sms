class SubjectRecipientModelMixin:

    @property
    def recipient_number(self):
        """Return a mobile number.

        Override to return a mobile number format: 26771111111.
        """
        return None
