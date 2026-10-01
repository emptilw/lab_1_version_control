import json
import random
import os

LEADERBOARD_FILE = "leaderboard.json"


def load_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        return []
    with open(LEADERBOARD_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_score(player_name, attempts):
    scores = load_leaderboard()
    scores.append({"name": player_name, "attempts": attempts})
    # Сортуємо за кількістю спроб (чим менше, тим краще)
    scores.sort(key=lambda x: x["attempts"])
    with open(LEADERBOARD_FILE, "w", encoding="utf-8") as f:
        json.dump(scores, f, ensure_ascii=False, indent=4)


def show_leaderboard():
    scores = load_leaderboard()
    if not scores:
        print("\n🏆 Таблиця рекордів порожня.")
        return

    print("\n🏆 --- ТАБЛИЦЯ РЕКОРДІВ ---")
    for idx, score in enumerate(scores[:5], 1):
        print(f"{idx}. {score['name']} — {score['attempts']} спроб(и)")


def play_game():
    print("\n🎮 Оберіть рівень складності:")
    print("1. Легкий (1 - 50)")
    print("2. Середній (1 - 100)")
    print("3. Важкий (1 - 200)")

    choice = input("Ваш вибір (1-3): ").strip()

    # БАГ №1: Для легкого рівня діапазон задається від 1 до 100 замість 1..50
    if choice == "1":
        max_num = 100  # <--- БАГ (має бути 50)
    elif choice == "2":
        max_num = 100
    elif choice == "3":
        max_num = 200
    else:
        print("Некоректний вибір. Встановлено середній рівень (1-100).")
        max_num = 100

    secret_number = random.randint(1, max_num)
    attempts = 0
    print(f"\nЯ загадав число від 1 до {max_num}. Спробуй вгадати!")

    while True:
        try:
            guess = int(input("Введіть ваше число: "))
            # БАГ №2: Спроби не підраховуються, оскільки змінна не оновлюється
            # attempts += 1  # <--- БАГ (рядок пропущено/закоментовано)

            if guess < secret_number:
                print("Загадане число БІЛЬШЕ ⬆️")
            elif guess > secret_number:
                print("Загадане число МЕНШЕ ⬇️")
            else:
                print(f"\n🎉 Вітаю! Ви вгадали число {secret_number} за {attempts} спроб!")
                player_name = input("Введіть ваше ім'я для таблиці рекордів: ").strip()
                if player_name:
                    save_score(player_name, attempts)
                break
        except ValueError:
            print("Будь ласка, введіть ціле число!")


def main():
    while True:
        print("\n=== ГРА 'ВГАДАЙ ЧИСЛО' ===")
        print("1. Почати гру")
        print("2. Переглянути таблицю рекордів")
        print("3. Вихід")

        choice = input("Оберіть дію (1-3): ").strip()

        if choice == "1":
            play_game()
        elif choice == "2":
            show_leaderboard()
        elif choice == "3":
            print("Дякуємо за гру! До побачення 👋")
            break
        else:
            print("Некоректний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()