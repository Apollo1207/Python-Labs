from classes.football_field import FootballField
from classes.athletics_field import AthleticsField
from classes.swimming_pool import SwimmingPool
from classes.roof_type import RoofType
from classes.purification_system_type import PurificationSystem
from manager.sport_build_manager import SportBuildManager


def main():
    sport_builds = [
        FootballField(950, 2001, "Lviv", 35, "football", RoofType.OPEN, "green", 52),
        AthleticsField(950, 2001, "Dnipro", 35, "athletics", 18, 9, "rubber"),
        SwimmingPool(950, 2001, "Kyiv", 35, "swimming", 2, 9, PurificationSystem.ULTRAVIOLET),
    ]

    manager = SportBuildManager(*sport_builds)


if __name__ == "__main__":
    main()
