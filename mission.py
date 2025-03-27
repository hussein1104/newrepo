class Mission:
    def __init__(self, name, description):
        self._name = name
        self._description = description
        self.mission_informations = f"Mission\nName: {self._name}\nDescription:{self._description}"
        self.db_name = ""
        self.db_engine = ""
    def set_db_name(self, name):
        self.db_name = name
    def set_db_engine(self, engine):
        self.db_engine = engine
    def __str__(self):
        return self.mission_informations
if __name__ == "__main__":
    mission = Mission("Alien Invasion", "Destroy the alien planet and save humanity")
    db_name = "******"
    db_engine = "******"
    mission.set_db_name(db_name)
    mission.set_db_engine(db_engine)
    print(mission)