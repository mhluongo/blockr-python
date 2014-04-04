"""
This module contains a collection of blockr API exeption classes.
"""

class ApiException(Exception):
    """ ApiExeption Class """
    def __init__(self, message):

        # Call the base class constructor with the parameters it needs
        Exception.__init__(self, message)

        # Now for your custom code...
        return message