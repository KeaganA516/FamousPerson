class FamousPerson:
    name = ""
    birth_year = ""
    country_of_birth = ""

    def __init__(self, name, birth_year, country_of_birth):
        self.name = name
        self.birth_year = birth_year
        self.country_of_birth = country_of_birth

    def __str__(self):
        return f"{self.name} was born in {self.birth_year} in {self.country_of_birth}."
    

class scientist(FamousPerson):
    field = ""
    notable_discovery = ""

    def __init__(self, name, birth_year, country_of_birth, field, notable_discovery):
        super().__init__(name, birth_year, country_of_birth)
        self.field = field
        self.notable_discovery = notable_discovery
    
    def __str__(self):
        return f"{self.name} was born in {self.birth_year} in {self.country_of_birth}. He was a scientist in the field of {self.field} and discovered {self.notable_discovery}."

class politician(FamousPerson):
    position = ""
    years_in_office = ""

    def __init__(self, name, birth_year, country_of_birth, position, years_in_office):
        super().__init__(name, birth_year, country_of_birth)
        self.position = position
        self.years_in_office = years_in_office
    
    def __str__(self):
        return f"{self.name} was born in {self.birth_year} in {self.country_of_birth}. He was a {self.position} and served for {self.years_in_office} years."

def introduce():
    print("Hello! Welcome to the Famous Person Database!")

def main():
    introduce()
    famousPerson1 = FamousPerson("Lebron James", "1984", "USA")
    famousPerson2 = scientist("Albert Einstein", "1879", "Germany", "Physics", "Theory of Relativity")
    famousPerson3 = politician("Abraham Lincoln", "1809", "USA", "President", "4")
    print(famousPerson1)
    print(famousPerson2)
    print(famousPerson3)

if __name__ == "__main__":

    main()