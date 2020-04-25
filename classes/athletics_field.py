from classes.sport_build import SportBuild


class AthleticsField(SportBuild):
    """Initialization subclass #2"""

    def __init__(self, number_of_seats, year_of_foundation, location, scale_of_field,
                 name_of_sport, count_of_sport_disciplines=None, count_of_running_tracks=None, type_of_field=None):
        super().__init__(number_of_seats, year_of_foundation, location, scale_of_field, name_of_sport)
        self.count_of_sport_disciplines = count_of_sport_disciplines
        self.count_of_running_tracks = count_of_running_tracks
        self.type_of_field = type_of_field

    def __del__(self):
        return

    def __str__(self):
        return super().__str__() + f"CountOfSportDisciplines:{self.count_of_sport_disciplines} CountOfRunningTracks:" \
                                   f"{self.count_of_running_tracks} TypeOfField:{self.type_of_field}"
