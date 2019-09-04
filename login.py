from location import Location


class User:
    @property
    def username(self):
        raise NotImplementedError

    def login(self):
        raise NotImplementedError

    def logout(self):
        raise NotImplementedError

    def update_email(self):
        raise NotImplementedError

    def update_password(self):
        raise NotImplementedError

    def set_timezone(self):
        raise NotImplementedError

    def get_locations(self):
        """Get the locations that a user has associated with their profile.
        """
        raise NotImplementedError

    def add_location(self, location: Location):
        """Add a new location to the users profile"""
        raise NotImplementedError
