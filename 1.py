from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = '7675064862:AAELbDw84mVvSEgmIyUHGyIRM-yMb286_yo'
app = Application.builder().token(TOKEN).build()


# Основне меню
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Соціал", callback_data='social')],
        [InlineKeyboardButton("OLX", callback_data='olx')],
        [InlineKeyboardButton("Shafa", callback_data='shafa')],
        [InlineKeyboardButton("Товари", callback_data='products')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.message:  # Якщо запит через команду /start
        await update.message.reply_text("Виберіть опцію:", reply_markup=reply_markup)
    elif update.callback_query:  # Якщо запит через callback (наприклад, кнопка "Повернутися назад")
        await update.callback_query.message.reply_text("Виберіть опцію:", reply_markup=reply_markup)


# Обробка кнопок
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # Видалення попереднього повідомлення
    await query.message.delete()

    if query.data == 'social':
        keyboard = [
            [InlineKeyboardButton("Конкурс", callback_data='contest')],
            [InlineKeyboardButton("Instagram", callback_data='instagram')],
            [InlineKeyboardButton("Facebook", callback_data='facebook')],
            [InlineKeyboardButton("Повернутися назад", callback_data='main_menu')]
        ]
        await query.message.reply_text("Соціальні мережі:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == 'olx':
        await query.message.reply_photo(
            photo="https://drive.google.com/uc?export=view&id=14hjS6RyWKJ4y9oI9igs8BjmHOlKZ-Ge0",
            caption="Перейти до наших оголошень на OLX:\n[Переглянути OLX](https://olx.ua)",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Повернутися назад", callback_data='main_menu')]])
        )

    elif query.data == 'shafa':
        await query.message.reply_photo(
            photo="https://drive.google.com/uc?export=view&id=14gIxVtNlHkm9HmHwIO9mizAfCgx0zsRV",
            caption="Перейти до наших оголошень на Shafa:\n[Переглянути Shafa](https://shafa.ua)",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Повернутися назад", callback_data='main_menu')]])
        )

    elif query.data == 'products':
        await query.message.reply_text("Тут будуть товари (завантажимо пізніше).", reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Повернутися назад", callback_data='main_menu')]]))

    elif query.data == 'contest':
        await query.message.reply_photo(
            photo="https://drive.google.com/uc?export=view&id=166ydt8yJ7d55xQKJTm-8tfbVjOf-uk_A",
            caption="Візьміть участь у конкурсі: [Переглянути конкурс](https://www.instagram.com/p/DBMGGlxs7Mm/)",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Повернутися назад", callback_data='social')]])
        )

    elif query.data == 'instagram':
        await query.message.reply_photo(
            photo="https://drive.google.com/uc?export=view&id=14tDBbRixB2-Jcu_NaQPErZxUz_07VBsr",
            caption="Наш Instagram: [Перейти в Instagram](https://www.instagram.com)",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Повернутися назад", callback_data='social')]])
        )

    elif query.data == 'facebook':
        await query.message.reply_photo(
            photo="https://drive.google.com/uc?export=view&id=150ZxQ-rQT155M3n1USLcs7pU0nutf3T8",
            caption="Наш Facebook: [Перейти у Facebook](https://www.facebook.com)",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Повернутися назад", callback_data='social')]])
        )

    elif query.data == 'main_menu':
        await start(update, context)


# Додавання обробників
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

app.run_polling()
