users = {
    "ivan":   {"password": "1111", "name": "Іван Петренко",  "grades": [12, 10, 8, 9, 11, 7, 10]},
    "olesya":  {"password": "2222", "name": "Олена Казмірчук",   "grades": [5, 6, 4, 2, 2, 4, 2, 2]},
    "andriy": {"password": "3333", "name": "Андрій Крищук",  "grades": [3, 2, 4, 1, 6, 4]},
    "maria":  {"password": "4444", "name": "Марія Бондар",   "grades": [11, 12, 12, 10, 9, 12]},
    "petro":  {"password": "5555", "name": "Петро Мельник",  "grades": [7, 4, 5, 3, 8, 6, 2, 9, 10]},
}
MAX_ATTEMPTS = 3

def authorize():

    for attempt in range(1, MAX_ATTEMPTS + 1):
        login = input("Логін: ").strip()
        password = input("Пароль: ").strip()

        if login in users and users[login]["password"] == password:
            return login

        left = MAX_ATTEMPTS - attempt
        if left > 0:
            print(f"Невірний логін або пароль. Залишилось спроб: {left}\n")
    return None


def show_grades(login):

    user = users[login]
    grades = user["grades"]

    satisfactory = sum(1 for g in grades if 5 <= g <= 12)   # від 5 до 12
    unsatisfactory = sum(1 for g in grades if 1 <= g <= 4)  # від 1 до 4

    print(f"\nВітаємо, {user['name']}!")
    print("Ваші оцінки:", ", ".join(map(str, grades)))
    print(f"Усього оцінок: {len(grades)}")
    print(f"Задовільних (5-12): {satisfactory}")
    print(f"Незадовільних (1-4): {unsatisfactory}")


def main():
    print("=== Електронний щоденник ===")
    while True:
        login = authorize()
        if login:
            show_grades(login)
        else:
            print("Кількість спроб вичерпано. Доступ заборонено.")

        again = input("\nВийти з програми? (т/н): ").strip().lower()
        if again == "т":
            print("До побачення!")
            break
        print()


if __name__ == "__main__":
    main()