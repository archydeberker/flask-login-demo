@dataclass
class Location:
    name: str
    activities: list
    coords: dict = None

    def _set_lat_and_long(self):
        """ Set the latitude and longitude associated
        with this location"""
        raise NotImplementedError

    def _set_activities(self, activities: list):
        """
        Set the activities associated with a given location.
        """
