import doctest
from classes import FootballField
from classes import AthleticsField
from classes import SwimmingPool
from classes import RoofType
from classes import PurificationSystem
from manager import SportBuildManager


class SportBuildManagerUtils:
    sport_builds_list = [FootballField(1, 1, "Lviv", 1, "football", RoofType.OPEN, "green", 52),
                         AthleticsField(2, 2, "Dnipro", 2, "athletics", 18, 9, "rubber"),
                         SwimmingPool(3, 3, "Kyiv", 3, "swimming", 2, 9, PurificationSystem.ULTRAVIOLET)]

    @staticmethod
    def sort_by_number_of_seats(reverse=None):
        """
        Sort by number of seats
        >>> sport_build_manager_object_utils.sort_by_number_of_seats(reverse=True)
        NumberOfSeats:3 YearOfFoundation:3 Location:Kyiv ScaleOfField:3 NameOfSport:swimming DepthOfPool:2 CountOfTracks:9 PurificationSystem:PurificationSystem.ULTRAVIOLETNumberOfSeats:2 YearOfFoundation:2 Location:Dnipro ScaleOfField:2 NameOfSport:athletics CountOfSportDisciplines:18 CountOfRunningTracks:9 TypeOfField:rubberNumberOfSeats:1 YearOfFoundation:1 Location:Lviv ScaleOfField:1 NameOfSport:football RoofType:RoofType.OPEN ColorOfField:green CountOfVipPlaces:52

        >>> sport_build_manager_object_utils.sort_by_number_of_seats(reverse=False)
        NumberOfSeats:1 YearOfFoundation:1 Location:Lviv ScaleOfField:1 NameOfSport:football RoofType:RoofType.OPEN ColorOfField:green CountOfVipPlaces:52NumberOfSeats:2 YearOfFoundation:2 Location:Dnipro ScaleOfField:2 NameOfSport:athletics CountOfSportDisciplines:18 CountOfRunningTracks:9 TypeOfField:rubberNumberOfSeats:3 YearOfFoundation:3 Location:Kyiv ScaleOfField:3 NameOfSport:swimming DepthOfPool:2 CountOfTracks:9 PurificationSystem:PurificationSystem.ULTRAVIOLET
        """
        sorted_items_by_number_of_seats = sorted(SportBuildManagerUtils.sport_builds_list,
                                                 key=lambda sport_build: sport_build.number_of_seats, reverse=reverse)
        return print("".join(str(a) for a in sorted_items_by_number_of_seats))

    @staticmethod
    def sort_by_year_of_foundation(reverse=None):
        """
         Sort by year of foundation
         >>> sport_build_manager_object_utils.sort_by_year_of_foundation(reverse=True)
         NumberOfSeats:3 YearOfFoundation:3 Location:Kyiv ScaleOfField:3 NameOfSport:swimming DepthOfPool:2 CountOfTracks:9 PurificationSystem:PurificationSystem.ULTRAVIOLETNumberOfSeats:2 YearOfFoundation:2 Location:Dnipro ScaleOfField:2 NameOfSport:athletics CountOfSportDisciplines:18 CountOfRunningTracks:9 TypeOfField:rubberNumberOfSeats:1 YearOfFoundation:1 Location:Lviv ScaleOfField:1 NameOfSport:football RoofType:RoofType.OPEN ColorOfField:green CountOfVipPlaces:52


        >>> sport_build_manager_object_utils.sort_by_year_of_foundation(reverse=False)
        NumberOfSeats:1 YearOfFoundation:1 Location:Lviv ScaleOfField:1 NameOfSport:football RoofType:RoofType.OPEN ColorOfField:green CountOfVipPlaces:52NumberOfSeats:2 YearOfFoundation:2 Location:Dnipro ScaleOfField:2 NameOfSport:athletics CountOfSportDisciplines:18 CountOfRunningTracks:9 TypeOfField:rubberNumberOfSeats:3 YearOfFoundation:3 Location:Kyiv ScaleOfField:3 NameOfSport:swimming DepthOfPool:2 CountOfTracks:9 PurificationSystem:PurificationSystem.ULTRAVIOLET
        """
        sorted_items_by_year_of_foundation = sorted(SportBuildManagerUtils.sport_builds_list,
                                                    key=lambda sport_build: sport_build.year_of_foundation,
                                                    reverse=reverse)
        return print("".join(str(b) for b in sorted_items_by_year_of_foundation))


if __name__ == "__main__":
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE, verbose=True,
                    extraglobs={'sport_build_manager_object_utils': SportBuildManagerUtils()})
