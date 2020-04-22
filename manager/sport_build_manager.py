class SportBuildManager:
    def __init__(self, sport_builds_list=None):
        if sport_builds_list is None:
            self.sport_builds_list = []
        else:
            self.sport_builds_list = sport_builds_list

    def sort_by_number_of_seats(self, reverse=True):
        return sorted(self.sport_builds_list, key=lambda sport_build: sport_build.number_of_seats, reverse=reverse)

    def sort_by_year_of_foundation(self, reverse=False):
        return sorted(self.sport_builds_list, key=lambda sport_build: sport_build.year_of_foundation, reverse=reverse)

    def find_by_name_of_sport(self, name_of_sport):
        return list(filter(lambda sport_build: sport_build.name_of_sport == name_of_sport, self.sport_builds_list))

    def find_by_scale_of_field(self, scale_of_field):
        return list(filter(lambda sport_build: sport_build.scale_of_field == scale_of_field, self.sport_builds_list))
