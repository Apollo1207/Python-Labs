from classes.sport_build import SportBuild


class FootballField(SportBuild):
    def __init__(self, number_of_seats, year_of_foundation, location, scale_of_field,
                 name_of_sport, color_of_field=None, count_of_vip_places=None):
        super().__init__(number_of_seats, year_of_foundation, location, scale_of_field, name_of_sport)
        # self.roof_type = roof_type
        self.color_of_field = color_of_field
        self.count_of_vip_places = count_of_vip_places
