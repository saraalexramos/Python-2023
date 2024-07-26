
class Musician():
    def __init__(self, name, instrument):
        self.__name = name
        self.__instrument = instrument
        self.__experience_level = 0
    
    def play(self):
        self.__experience_level += 1

    def experience(self):
        return self.__experience_level
    
    def get_name (self):
        return self.__name
    
    def get_instrument(self):
        return self.__instrument

    def __str__(self):
        return f"{self.__name}, instrument: {self.__instrument}. Experience: {self.__experience_level}"


class Orchestra():
    def __init__(self):
        self.__musicians = []
        self.__play_count = 0

    def add_musician(self, musician: Musician):
        self.__musicians.append(musician)  

    def play(self):
        self.__play_count += 1
        for musician in self.__musicians:
            musician.play()

    def __str__(self):
        average_experience = sum(musician.experience() for musician in self.__musicians) / len(self.__musicians)
        result = f"Orchestra (played {self.__play_count} times, average experience of members: {average_experience}) \n"
        result += "\n".join(str(musician) for musician in self.__musicians)
        return result


if __name__ == "__main__":
    adam = Musician("Adam", "Tuba")
    steve = Musician("Steve", "Banjo")

    orchestra = Orchestra()
    orchestra.add_musician(adam)
    orchestra.add_musician(steve)

    print(orchestra)

    orchestra.play()

    print()
    print(orchestra)

    adam.play()

    print()
    print(orchestra)

    madonna = Musician("Madonna", "Piano")
    orchestra.add_musician(madonna)
    orchestra.play()

    print()
    print(orchestra)