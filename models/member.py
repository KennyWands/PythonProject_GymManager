class Member:
    def __init__(self, get_name, get_membership, get_active, get_id=None):
        self.name = get_name
        self.membership = get_membership
        self.active = get_active
        self.id = get_id
