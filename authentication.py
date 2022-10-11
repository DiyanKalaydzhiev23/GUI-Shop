from canvas import *
from helpers import clean_screen
from json import dump, loads
from buying_page import display_products


def render_entry():
    register_btn = Button(root, text="Register", bg="green", fg="white", borderwidth=0,
                          width=20, height=3, command=register)
    login_btn = Button(root, text="Login", bg="blue", fg="white", borderwidth=0, width=20, height=3, command=login)

    frame.create_window(350, 260, window=register_btn)
    frame.create_window(350, 320, window=login_btn)


def login():
    global username_box, password_box
    clean_screen()

    frame.create_text(100, 50, text="Username:")
    frame.create_text(100, 100, text="Password:")

    frame.create_window(200, 50, window=username_box)
    frame.create_window(200, 100, window=password_box)

    logging_btn = Button(root, text="Login", bg="blue", fg="white", command=logging)
    frame.create_window(250, 150, window=logging_btn)


def logging():
    if check_logging():
        display_products()
    else:
        frame.create_text(175, 200, text="Invalid username or password!", fill="red")


def check_logging():
    global username_box, password_box

    info = []
    with open("db/users_information.json", "r") as user_file:
        for line in user_file:
            info.append(loads(line))

    for i in range(len(info)):
        username = info[i]['username']
        password = info[i]['password']
        if username == username_box.get() and password == password_box.get():
            return True
    return False


def register():
    global firstname_box, lastname_box, username_box, password_box
    clean_screen()

    frame.create_text(100, 50, text="First name:")
    frame.create_text(100, 100, text="Last name:")
    frame.create_text(100, 150, text="Username:")
    frame.create_text(100, 200, text="Password:")

    frame.create_window(200, 50, window=firstname_box)
    frame.create_window(200, 100, window=lastname_box)
    frame.create_window(200, 150, window=username_box)
    frame.create_window(200, 200, window=password_box)

    registration_btn = Button(root, text="Register", bg="green", fg="white", command=registration)
    frame.create_window(300, 250, window=registration_btn)


def registration():
    global info_dict

    info_dict = {"firstname": firstname_box.get(),
                 "lastname": lastname_box.get(),
                 "username": username_box.get(),
                 "password": password_box.get(),
                 "products": []}

    if check_registration():
        with open("db/users_information.json", "a") as user_file:
            dump(info_dict, user_file)
            user_file.write("\n")
            display_products()


def check_registration():
    global info_dict

    for el in info_dict.values():
        if el == "":
            frame.create_text(300, 300, text="We are missing information, please check your fields!",
                              fill="red", tag="error")
            return False
    else:
        frame.delete("error")

    info = []
    with open("db/users_information.json", "r") as user_file:
        for line in user_file:
            info.append(loads(line))

    for i in range(len(info)):
        if info[i]['username'] == info_dict['username']:
            frame.create_text(300, 300, text="Username already exists!", fill="red", tag="error")
            return False
    else:
        frame.delete("error")
    return True


firstname_box = Entry(root, bd=0)
lastname_box = Entry(root, bd=0)
username_box = Entry(root, bd=0)
password_box = Entry(root, bd=0)
