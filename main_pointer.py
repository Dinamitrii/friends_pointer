import time
import datetime


def age_calculator(date):
    today = datetime.date.today()
    age_old = (today - birthdate) // datetime.timedelta(days=365.2425)
    return age_old


birthdate = datetime.date(1989, 4, 30)
age = age_calculator(birthdate)

pointer_list_with_dictionaries_for_friends = [{
    "name": "Никола",
    "last_name": "Янков",
    "nickname": "Шкумбата",
    "birthday": birthdate,
    "years_old": age,
    "phone": "+359885440030",
    "city": "София",
    "district": "Дианабад",
    "postal_code": 1172,
    "address": "блок 29 етаж 3"
}]

current_time = time.time()
time_string = time.ctime(current_time)
print("Current time: ", time_string)


def full_info(na, ln, ni, bi, yo, ci, di, pc, add, ph) -> list:
    name = pointer_list_with_dictionaries_for_friends[0].get("name")
    lastname = pointer_list_with_dictionaries_for_friends[0].get("last_name")
    city = pointer_list_with_dictionaries_for_friends[0].get("city")
    district = pointer_list_with_dictionaries_for_friends[0].get("district")
    postal_code = pointer_list_with_dictionaries_for_friends[0].get("postal_code")
    address = pointer_list_with_dictionaries_for_friends[0].get("address")
    birthday = pointer_list_with_dictionaries_for_friends[0].get("birthday")
    phone = pointer_list_with_dictionaries_for_friends[0].get("phone")
    years_old = pointer_list_with_dictionaries_for_friends[0].get("years_old")
    nickname = pointer_list_with_dictionaries_for_friends[0].get("nickname")

    result = [name, lastname, nickname, birthday, years_old, "Годишен", city, district, postal_code, address, phone]
    return result


print(full_info(na=1, ln=2, ni=3, bi=4, yo=5, ci=6, di=7, pc=8, add=9, ph=10))
