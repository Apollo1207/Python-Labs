from classes import FootballField
from classes import AthleticsField
from classes import SwimmingPool
from classes import RoofType
from classes import PurificationSystem
from manager import SportBuildManager


def main():
    sport_builds_list = [
        FootballField(1, 1, "Lviv", 1, "football", RoofType.OPEN, "green", 52),
        AthleticsField(2, 2, "Dnipro", 2, "athletics", 18, 9, "rubber"),
        SwimmingPool(3, 3, "Kyiv", 3, "swimming", 2, 9, PurificationSystem.ULTRAVIOLET)
    ]

    sport_build_manager = SportBuildManager(sport_builds_list)

    method_calls_list = [sport_build_manager.sort_by_number_of_seats(),
                         sport_build_manager.sort_by_year_of_foundation(),
                         sport_build_manager.find_by_name_of_sport(name_of_sport="swimming"),
                         sport_build_manager.find_by_scale_of_field(scale_of_field=2)
                         ]

    output_processed_lists(method_calls_list)


def output_processed_lists(method_calls_list):
    for obj in method_calls_list:
        print("".join(str(x) for x in obj))


if __name__ == "__main__":
    main()
