class Mission:
    def __init__(self, name, description):
        self._name = name
        self._description = description
        self.mission_informations = f"Mission\nName: {self._name}\nDescription:{self._description}"


if __name__ == "__main__":
    mission = Mission("Alien Invasion", "Destroy the alien planet and save humanity")
    print(mission.mission_informations)