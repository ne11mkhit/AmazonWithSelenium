class VariablesClass:
    __username = "vicisarkissian@gmail.com"
    __password = "vici123456654321!"
    searchText = "Globe"
    amazonSignInURL = "https://www.amazon.com/gp/sign-in.html"

    @classmethod
    def get_username(cls):
        return cls.__username

    @classmethod
    def get_password(cls):
        return cls.__password
