from gupshup_api.query_params import QueryParams


class OptIn(QueryParams):
    """Query parameters for opting-in a user"""

    user = 'user', 'User phone number'
