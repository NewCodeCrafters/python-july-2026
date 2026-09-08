class Employee:
    # Class attribute (shared)
    company = "TechCorp"

    def __init__(self, name, salary, specialization):
        # Instance attributes (unique)
        self.name = name
        self.specialization = specialization
        self.salary = salary
        self._bonus = 0  # Encapsulated (Benefit: Security)
        self._penalty = 0

    # Method to safely modify the hidden attribute
    def set_bonus(self, amount):
        if amount > 0:
            self._bonus = amount
        else:
            print("Bonus must be positive!")

    def set_penalty(self, percentage):
        if percentage > 0 and percentage <= 1:
            self._penalty = percentage * self.salary
        else:
            print("Penalty percentage must not be less than 0 or more than 1")

    def total_pay(self):
        return self.salary + self._bonus - self._penalty

    def introduce(self):
        return f"I am {self.name}. I work at {self.company}. I work as a/an {self.specialization}. My total Pay is {self.total_pay()}"

obj1 = Employee(name="Fikayo", salary=200000,specialization="AI engineer")
obj2 = Employee(name="Destiny", salary=200000,specialization="Cyber Analyst")
obj3 = Employee(name="Peter", salary=200000,specialization="Backend Development")
obj4 = Employee(name="Ore", salary=200000,specialization="AI Engineering")

obj4.set_penalty(0.45)
obj4.set_bonus(40000)
obj4.company = "NCC"
print(obj4.introduce())
print(obj1.introduce())


# Inheritance (Benefit: Reusability)

class Manager(Employee):
    def __init__(self, name, salary, position, team_size):
        super().__init__(name, salary, position)  # Reuse parent attributes
        self.team_size = team_size      # New attribute


    def introduce(self):
        return f"I am {self.name}. I work as a manager at {self.company}. I work as a/an {self.specialization}. My total Pay is {self.total_pay()}. My team size is {self.team_size}"

# Usage
alice = Manager("Alice", 600000, "Executive VP of Engineering", team_size=19)
alice.set_bonus(500000)
print(alice.introduce())

# print(f"{alice.name} works at {alice.company}") # Output: Alice works at TechCorp
# print(f"Total Pay: ${alice.total_pay()}")       # Output: Total Pay: $65000