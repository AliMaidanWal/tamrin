from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import random


class NumberGame(App):

    def build(self):
        self.number = random.randint(1, 10)
        self.attempts = 0

        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=15
        )

        title = Label(
            text="🎮 بازی حدس عدد",
            font_size=28
        )
        layout.add_widget(title)

        info = Label(
            text="یک عدد بین 1 تا 10 حدس بزن!",
            font_size=18
        )
        layout.add_widget(info)

        self.input_box = TextInput(
            hint_text="عدد را وارد کن",
            input_filter="int",
            multiline=False,
            font_size=24,
            halign="center"
        )
        layout.add_widget(self.input_box)

        guess_button = Button(
            text="🎯 حدس بزن",
            font_size=20
        )
        guess_button.bind(on_press=self.check_guess)
        layout.add_widget(guess_button)

        self.result = Label(
            text="آماده‌ای؟",
            font_size=18
        )
        layout.add_widget(self.result)

        self.score_label = Label(
            text="تلاش‌ها: 0 | امتیاز: 0",
            font_size=18
        )
        layout.add_widget(self.score_label)

        restart_button = Button(
            text="🔄 بازی دوباره",
            font_size=20
        )
        restart_button.bind(on_press=self.restart)
        layout.add_widget(restart_button)

        return layout

    def check_guess(self, instance):
        value = self.input_box.text.strip()

        if not value:
            self.result.text = "⚠️ اول یک عدد وارد کن!"
            return

        guess = int(value)

        if guess < 1 or guess > 10:
            self.result.text = "⚠️ فقط عدد 1 تا 10!"
            return

        self.attempts += 1

        if guess == self.number:
            score = max(10, 100 - (self.attempts - 1) * 10)
            self.result.text = "🎉 آفرین! درست حدس زدی!"
            self.score_label.text = (
                f"تلاش‌ها: {self.attempts} | امتیاز: {score}"
            )

        elif guess < self.number:
            self.result.text = "⬆️ عدد بزرگ‌تر است!"
            self.score_label.text = (
                f"تلاش‌ها: {self.attempts} | امتیاز: 0"
            )

        else:
            self.result.text = "⬇️ عدد کوچک‌تر است!"
            self.score_label.text = (
                f"تلاش‌ها: {self.attempts} | امتیاز: 0"
            )

        self.input_box.text = ""

    def restart(self, instance):
        self.number = random.randint(1, 10)
        self.attempts = 0
        self.input_box.text = ""
        self.result.text = "عدد جدید انتخاب شد! 🎯"
        self.score_label.text = "تلاش‌ها: 0 | امتیاز: 0"


if __name__ == "__main__":
    NumberGame().run()
