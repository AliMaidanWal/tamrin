import random

print("🎮 بازی حدس عدد")

while True:
    number = random.randint(1, 10)
    attempts = 0

    print("من یک عدد بین 1 تا 10 انتخاب کرده‌ام.")

    while True:
        guess = int(input("حدس تو: "))

        if guess < 1 or guess > 10:
            print("⚠️ فقط عددی بین 1 تا 10 وارد کن!")
            continue

        attempts += 1

        if guess == number:
            score = 100 - (attempts - 1) * 10
            print("🎉 آفرین! درست حدس زدی!")
            print("تعداد تلاش‌ها:", attempts)
            print("امتیاز:", score)
            break
        else:
            print("❌ اشتباه بود!")
            print("دوباره حدس بزن!")

    play_again = input("بازی دوباره؟ (y/n): ")

    if play_again.lower() != "y":
        print("👋 خداحافظ!")
        break
