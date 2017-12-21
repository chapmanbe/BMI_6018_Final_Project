"""This is the Calorie class that will be imported into the Calorie Tracker program"""
class Calorie:
    """Calorie class that gets the user's gender, weight, height, and age to determine the amount of
    calories they should be consuming each day"""
    def __init__(self):
        self.m_gender = ""
        self.m_weight = 0
        self.m_height = 0
        self.m_age = 0
        self.m_balance = 0

    def set_gender(self):
        """Sets the user's gender"""
        self.m_gender = input("What is your gender (F or M)? ")
        while self.m_gender.lower() != "f" and self.m_gender.lower() != "m":
            print ("Please choose a valid option (F or M).  ")
            self.m_gender = input("What is your gender (F or M)? ")
        return self.m_gender

    def set_weight(self):
        """Sets the user's weight"""
        self.m_weight = input("How much do you weigh in pounds? ")
        return self.m_weight

    def set_height(self):
        """Sets the user's height"""
        self.m_height = input("How tall are you in inches? ")
        return self.m_height

    def set_age(self):
        """Sets the user's age"""
        self.m_age = input("How old are you? ")
        return self.m_age


    def set_balance(self, gender, height, weight, age):
        """Sets the calorie balance based on the user's information"""
        if gender == "m":
            bmr = 66 + (12.7 * float(height)) + (6.23 * float(weight)) - (6.8 * float(age))
            self.m_balance -= bmr
        else:
            bmr = 655 + (4.7 * float(height)) + (4.35 * float(weight)) - (4.7 * float(age))
            self.m_balance -= bmr
        return round(self.m_balance, 2)

    def get_gender(self):
        """returns the user's gender"""
        return self.m_gender

    def get_weight(self):
        """returns the user's weight"""
        return self.m_weight

    def get_height(self):
        """returns the user's height"""
        return self.m_height

    def get_age(self):
        """returns the user's age"""
        return self.m_age

    def get_balance(self):
        """returns current calorie balance"""
        return round(self.m_balance, 2)

    def eat(self, amount):
        """adds to calorie balance"""
        self.m_balance += float(amount)
        return self.m_balance

    def basketball(self, weight):
        """calories burned from playing basketball"""
        time = input("how long did you perform this activity in minutes? ")
        burned = .063 * float(weight) * float(time)
        self.m_balance -= burned
        return self.m_balance

    def jump_rope(self, weight):
        """calories burned from jumping rope"""
        time = input("how long did you perform this activity in minutes? ")
        burned = .080 * float(weight) * float(time)
        self.m_balance -= burned
        return self.m_balance

    def running(self, weight):
        """calories burned from running"""
        time = input("how long did you perform this activity in minutes? ")
        burned = .095 * float(weight) * float(time)
        self.m_balance -= burned
        return self.m_balance


    def walking(self, weight):
        """calories burned from walking"""
        time = input("how long did you perform this activity in minutes? ")
        burned = .036 * float(weight) * float(time)
        self.m_balance -= burned
        return self.m_balance

    def weight_training(self, weight):
        """calories burned from lifting weights"""
        time = input("how long did you perform this activity in minutes? ")
        burned = .039 * float(weight) * float(time)
        self.m_balance -= burned
        return self.m_balance
