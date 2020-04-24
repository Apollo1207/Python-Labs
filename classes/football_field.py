from classes.sport_build import SportBuild
from classes.roof_type import RoofType


class FootballField(SportBuild):
    """Initialization subclass #1"""

    def __init__(self, number_of_seats, year_of_foundation, location, scale_of_field,
                 name_of_sport, roof_type=None, color_of_field=None, count_of_vip_places=None):
        super().__init__(number_of_seats, year_of_foundation, location, scale_of_field, name_of_sport)
        self.roof_type = roof_type
        self.color_of_field = color_of_field
        self.count_of_vip_places = count_of_vip_places

    def __del__(self):
        return

    def __str__(self):
        return f"NumberOfSeats:{self.number_of_seats} YearOfFoundation:{self.year_of_foundation}" \
               f" Location:{self.location} ScaleOfField:{self.scale_of_field} NameOfSport:" \
               f"{self.name_of_sport} RoofType:{self.roof_type} ColorOfField:" \
               f"{self.color_of_field} CountOfVipPlaces:{self.count_of_vip_places}"
