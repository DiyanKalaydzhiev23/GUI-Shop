from json import loads, dump

from buying_page import display_products
from canvas import *
from helpers import clean_screen


def get_all_users_data():
    info_data = []

    with open("db/users_information.json", "r") as users_file:
        for line in users_file:
            info_data.append(loads(line))

    return info_data


def render_entry():
    register_btn = Button(
        root,
        text="Register",
        bg="green",
        fg="white",
        borderwidth=0,
        width=20,
        height=3,
        command=register,
    )

    login_btn = Button(
        root,
        text="Login",
        bg="blue",
        fg="white",
        width=20,
        height=3,
        command=login
    )

    frame.create_window(350, 260, window=register_btn)
    frame.create_window(350, 320, window=login_btn)


def login():
    clean_screen()

    frame.create_text(100, 50, text="Username:")
    frame.create_text(100, 100, text="Password:")

    frame.create_window(200, 50, window=username_box)
    frame.create_window(200, 100, window=password_box)

    logging_btn = Button(
        root,
        text="Login",
        bg="blue",
        fg="white",
        command=logging
    )
    frame.create_window(250, 150, window=logging_btn)


def logging():
    if check_logging():
        display_products()
    else:
        frame.create_text(160, 200, text="Invalid username or password!", fill="red")


def check_logging():
    info_data = get_all_users_data()

    for i in range(len(info_data)):
        username = info_data[i]["username"]
        password = info_data[i]["password"]

        if username == username_box.get() and password == password_box.get():
            return True

    return False


def register():
    clean_screen()

    frame.create_text(100, 50, text="First name:")
    frame.create_text(100, 100, text="Last name:")
    frame.create_text(100, 150, text="Username:")
    frame.create_text(100, 200, text="Password:")

    frame.create_window(200, 50, window=first_name_box)
    frame.create_window(200, 100, window=last_name_box)
    frame.create_window(200, 150, window=username_box)
    frame.create_window(200, 200, window=password_box)

    registration_btn = Button(
        root,
        text="Register",
        bg="green",
        fg="white",
        command=registration
    )
    frame.create_window(300, 250, window=registration_btn)


def registration():
    info_dict = {
        "first_name": first_name_box.get(),
        "last_name": last_name_box.get(),
        "username": username_box.get(),
        "password": password_box.get(),
        "products": []
    }

    if check_registration(info_dict):
        with open("db/users_information.json", "a") as users_file:
            dump(info_dict, users_file)
            users_file.write("\n")
            display_products()


def check_registration(info):
    for el in list(info.values())[:-1]:
        if el.strip() == "":
            frame.create_text(
                300,
                300,
                text="We are missing some information, please check your fields!",
                fill="red",
                tag="error",
            )

            return False

    frame.delete("error")

    info_data = get_all_users_data()

    for i in range(len(info_data)):
        if info_data[i]['username'] == info['username']:
            frame.create_text(
                300,
                300,
                text="Username already exists!",
                fill="red",
                tag="error",
            )
            return False

    frame.delete("error")

    return True


first_name_box = Entry(root, bd=0)
last_name_box = Entry(root, bd=0)
username_box = Entry(root, bd=0)
password_box = Entry(root, bd=0, show="*")
