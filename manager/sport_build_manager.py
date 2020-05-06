from classes import FootballField
from classes import AthleticsField
from classes import SwimmingPool
from classes import RoofType
from classes import PurificationSystem


class SportBuildManager:
    def __init__(self, sport_builds_list=None):
        if sport_builds_list is None:
            self.sport_builds_list = []
        else:
            self.sport_builds_list = sport_builds_list

    def find_by_name_of_sport(self, name_of_sport):
        """
        >>> sport_build_manager_object.find_by_name_of_sport("football")
        NumberOfSeats:1 YearOfFoundation:1 Location:Lviv ScaleOfField:1 NameOfSport:football RoofType:RoofType.OPEN ColorOfField:green CountOfVipPlaces:52

        >>> sport_build_manager_object.find_by_name_of_sport("athletics")
        NumberOfSeats:2 YearOfFoundation:2 Location:Dnipro ScaleOfField:2 NameOfSport:athletics CountOfSportDisciplines:18 CountOfRunningTracks:9 TypeOfField:rubber

        >>> sport_build_manager_object.find_by_name_of_sport("swimming")
        NumberOfSeats:3 YearOfFoundation:3 Location:Kyiv ScaleOfField:3 NameOfSport:swimming DepthOfPool:2 CountOfTracks:9 PurificationSystem:PurificationSystem.ULTRAVIOLET
        """
        found_items_by_name_of_sport = list(
            filter(lambda sport_build: sport_build.name_of_sport == name_of_sport, self.sport_builds_list))
        return print("".join(str(c) for c in found_items_by_name_of_sport))

    def find_by_scale_of_field(self, scale_of_field):
        """
        >>> sport_build_manager_object.find_by_scale_of_field(2)
        NumberOfSeats:2 YearOfFoundation:2 Location:Dnipro ScaleOfField:2 NameOfSport:athletics CountOfSportDisciplines:18 CountOfRunningTracks:9 TypeOfField:rubber

         >>> sport_build_manager_object.find_by_scale_of_field(1)
         NumberOfSeats:1 YearOfFoundation:1 Location:Lviv ScaleOfField:1 NameOfSport:football RoofType:RoofType.OPEN ColorOfField:green CountOfVipPlaces:52

         >>> sport_build_manager_object.find_by_scale_of_field(3)
         NumberOfSeats:3 YearOfFoundation:3 Location:Kyiv ScaleOfField:3 NameOfSport:swimming DepthOfPool:2 CountOfTracks:9 PurificationSystem:PurificationSystem.ULTRAVIOLET
         """
        found_items_by_scale_of_field = list(
            filter(lambda sport_build: sport_build.scale_of_field == scale_of_field, self.sport_builds_list))
        return print("".join(str(d) for d in found_items_by_scale_of_field))


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE, verbose=True,
                    extraglobs={'sport_build_manager_object': SportBuildManager(
                        sport_builds_list=[FootballField(1, 1, "Lviv", 1, "football", RoofType.OPEN, "green", 52),
                                           AthleticsField(2, 2, "Dnipro", 2, "athletics", 18, 9, "rubber"),
                                           SwimmingPool(3, 3, "Kyiv", 3, "swimming", 2, 9,
                                                        PurificationSystem.ULTRAVIOLET)])})
