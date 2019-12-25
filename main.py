import windows_init
from jcUserClass import User

if __name__ == "__main__":
    main_user = User(("id", "name", "type", "comp",
                      "", "password", "pd", "0.0"))
    windows_init.show_login(main_user)
