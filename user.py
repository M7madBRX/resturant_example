class User:
    def __init__(self, first_name, last_name, year_level, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.year_level = year_level
        self.salary = salary
        self.login_attempts = 0  # تصحيح اسم المتغير

    def describe_user(self):
        print(f"Her First Name is {self.first_name}, her last name is {self.last_name}, year level {self.year_level}, salary {self.salary}")

    def greeting(self):
        print(f"HELLO {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1
        if self.login_attempts >= 5:
            print("You are a hacker!")

    def reset_login_attempts(self):
        self.login_attempts = 0

# إنشاء كائن من الفئة User
greeting = User("Eman", "Shaouq", "Senior", "Over 1k")

# استخدام الدوال
greeting.greeting()
greeting.describe_user()

# زيادة عدد المحاولات
greeting.increment_login_attempts()
greeting.increment_login_attempts()
greeting.increment_login_attempts()
greeting.increment_login_attempts()
greeting.increment_login_attempts()
greeting.increment_login_attempts()  # سيطبع "You are a hacker!"

# طباعة عدد المحاولات
print(f"user attempts: {greeting.login_attempts}")
greeting.reset_login_attempts()
print(f"user attempts: {greeting.login_attempts}")
