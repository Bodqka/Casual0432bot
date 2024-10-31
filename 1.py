from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Токен вашого бота
TOKEN = "6851274116:AAGP79m6lWf44I6l9pnZSDyUVM23M68d7DQ"
ADMIN_ID = 5145857737


# Функція для стартового повідомлення
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo_url = "https://drive.google.com/uc?export=view&id=1x7CXxTLX1e4_reBY_q4znCyLLxtaDenK"
    await update.message.reply_photo(photo_url,
                                     caption="Привіт я Casual0432. Пропоную брендовий одяг по низьких цінах🔥\n\n"
                                             "Використовуйте команду /menu для перегляду доступних опцій.")


# Функція для меню команд
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Доступні команди:\n"
        "/olx - Переглянути оголошення на OLX\n"
        "/shafa - Переглянути оголошення на Shafa\n"
        "/social - Соціальні мережі\n"
        "/faq - Часті запитання\n"
        "/giveaway - Участь у конкурсі\n"
        "/contact_support - Зв'язатися з підтримкою"
    )


# Команда для відображення оголошень на OLX
async def olx(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo_url = "https://drive.google.com/uc?export=view&id=14hjS6RyWKJ4y9oI9igs8BjmHOlKZ-Ge0"
    await update.message.reply_photo(photo_url,
                                     caption="Сторінка на OLX: https://www.olx.ua/uk/list/user/vXRAm/")


# Команда для відображення оголошень на Shafa
async def shafa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo_url = "https://drive.google.com/uc?export=view&id=14gIxVtNlHkm9HmHwIO9mizAfCgx0zsRV"
    await update.message.reply_photo(photo_url,
                                     caption="Сторінка на Shafa: https://shafa.ua/uk/member/nechto7inoe")


# Команда для соціальних мереж
async def social(update: Update, context: ContextTypes.DEFAULT_TYPE):
    instagram_photo_url = "https://drive.google.com/uc?export=view&id=14tDBbRixB2-Jcu_NaQPErZxUz_07VBsr"
    facebook_photo_url = "https://drive.google.com/uc?export=view&id=150ZxQ-rQT155M3n1USLcs7pU0nutf3T8"

    await update.message.reply_photo(instagram_photo_url,
                                     caption="Instagram: https://www.instagram.com/casual.0432 - Підписуйтесь на нашу сторінку в Instagram ❌")
    await update.message.reply_photo(facebook_photo_url,
                                     caption="Facebook: https://www.facebook.com/share/Wf4Ly4cMt2a8qE9o - Додавайтесь у друзі до нас на Facebook 📌")


# Команда для частих запитань
async def faq(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "FAQ - Коротенько та ясно:) \n\n"
        "1. Як замовити?\n"
        "- Замовлення здійснюється на сайтах OLX або Shafa, де доступні різні способи оплати.\n\n"
        "2. Чи продаю без сайтів?\n"
        "- Так, можете зв'язатися безпосередньо та обговоримо це питання. ➡️ @casual0432_support\n\n"
        "3. Чи існує повернення товару?\n"
        "- Так, існує, все залежить від ситуації. В будь-якому випадку проблему вирішимо. ➡️ @casual0432_support "
    )


# Команда для участі в конкурсі
async def giveaway(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo_url = "https://drive.google.com/uc?export=view&id=166ydt8yJ7d55xQKJTm-8tfbVjOf-uk_A"
    await update.message.reply_photo(photo_url, caption="Розіграш! у моєму Instagram: https://www.instagram.com/reel/DBMGGlxs7Mm/?igshid=MWNzdTM4ZnpyNmpubw==")


# Команда для контакту з підтримкою
async def contact_support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Зворотній зв'язок: @casual0432_support")


# Основна функція для запуску бота
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    # Команда старту
    app.add_handler(CommandHandler("start", start))

    # Команда меню
    app.add_handler(CommandHandler("menu", menu))

    # Команди для кожної функції
    app.add_handler(CommandHandler("olx", olx))
    app.add_handler(CommandHandler("shafa", shafa))
    app.add_handler(CommandHandler("social", social))
    app.add_handler(CommandHandler("faq", faq))
    app.add_handler(CommandHandler("giveaway", giveaway))
    app.add_handler(CommandHandler("contact_support", contact_support))

    # Запуск бота
    app.run_polling()