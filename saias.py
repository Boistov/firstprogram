class Person:
    def __init__(self, name, surname, birthdate, country, city, region, profession, gender):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.country = country
        self.city = city
        self.region = region
        self.profession = profession
        self.gender = gender
    
    def get_info(self):
        return f"person: {self.name} {self.surname}, birth: {self.birthdate}, Country: {self.country}, city: {self.city}, region: {self.region}, job: {self.profession}, sex: {self.gender}"


class User(Person):
    def __init__(self, name, surname, birthdate, country, city, region, profession, gender, username, password):
        super().__init__(name, surname, birthdate, country, city, region, profession, gender)
        self.username = username
        self.password = password

    def get_user_info(self):
        return f"{self.username}, {self.password}, {self.name}, {self.surname}, {self.birthdate}, {self.country}, {self.city}, {self.region}, {self.profession}, {self.gender}"


class UserManager:
    def __init__(self):
        self.users = []

    def signup(self):
        name = input("name: ")
        surname = input("Surname: ")
        birthdate = input("birthdate: ")
        country = input("Country: ")
        city = input("City: ")
        region = input("Region: ")
        profession = input("Profession: ")
        gender = input("Gender: ")
        username = input("username: ")
        password = input("password: ")
        
        user = User(name, surname, birthdate, country, city, region, profession, gender, username, password)
        self.users.append(user)
        self.save_users()
    
    def login(self):
        username = input("username: ")
        password = input("password: ")
        user_found = False
        for user in self.users:
            if user.username == username:
                if user.password == password:
                    print("You login in successfully")
                    print(user.get_info())
                    user_found = True
                else: 
                    print("Wrong password")
                    user_found = True
        if not user_found:
            print("We don't have this username in our database")
    
    def change_password(self):
        username = input("username: ")
        old_password = input("old password: ")
        user_found = False
        for user in self.users:
            if user.username == username and user.password == old_password:
                new_password = input("new password: ")
                user.password = new_password
                print("your password changed")
                user_found = True
                self.save_users()
                break
        if not user_found:
            print("password is incorrect")
    
    def save_users(self):
        with open("users.txt", 'a') as file:
            for user in self.users:
                file.write(user.get_user_info() + "\n")
    
    def get_users(self):
        for user in self.users:
            print(user.get_info())
    
    def main(self):
        while True:
            print("1. Signup")
            print("2. Login")
            print("3. Get users")
            print("4. Change password")
            print("5. Save")
            choice = input("Choose an option: ")
            if choice == '1':
                self.signup()
            elif choice == '2':
                self.login()
            elif choice == '3':
                self.get_users()
            elif choice == '4':
                self.change_password()
            elif choice == '5':
                self.save_users()
                break
            else:
                print("Please try again")


manager = UserManager()
manager.main()

