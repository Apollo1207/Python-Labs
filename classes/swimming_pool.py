from classes.sport_build import SportBuild


class SwimmingPool(SportBuild):

    def __init__(self, number_of_seats, year_of_foundation, location, scale_of_field,
                 name_of_sport, depth_of_pool=None, count_of_tracks=None):
        super().__init__(number_of_seats, year_of_foundation, location, scale_of_field, name_of_sport)
        self.depth_of_pool = depth_of_pool
        self.count_of_tracks = count_of_tracks
        # self.Sun = Sun
