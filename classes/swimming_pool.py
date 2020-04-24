from classes.sport_build import SportBuild
from classes.purification_system_type import PurificationSystem


class SwimmingPool(SportBuild):
    """Initialization subclass #3"""

    def __init__(self, number_of_seats, year_of_foundation, location, scale_of_field,
                 name_of_sport, depth_of_pool=None,
                 count_of_tracks=None, purification_system=None):
        super().__init__(number_of_seats, year_of_foundation, location, scale_of_field, name_of_sport)
        self.depth_of_pool = depth_of_pool
        self.count_of_tracks = count_of_tracks
        self.purification_system = purification_system

    def __del__(self):
        return

    def __str__(self):
        return f"NumberOfSeats:{self.number_of_seats} YearOfFoundation:{self.year_of_foundation}"\
               f" Location:{self.location} ScaleOfField:{self.scale_of_field} NameOfSport:" \
               f"{self.name_of_sport} DepthOfPool:{self.depth_of_pool} CountOfTracks:" \
               f"{self.count_of_tracks} PurificationSystem:{self.purification_system}"
