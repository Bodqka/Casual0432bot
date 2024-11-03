from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = '7675064862:AAELbDw84mVvSEgmIyUHGyIRM-yMb286_yo'
app = Application.builder().token(TOKEN).build()

# Основне меню
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Соціальні мережі👥", callback_data='social')],
        [InlineKeyboardButton("Товари👕👖👟", callback_data='products')],
        [InlineKeyboardButton("Підтримка🆘", callback_data='support')],
        [InlineKeyboardButton("Конкурс🏆", callback_data='contest')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.message:
        await update.message.reply_text("Виберіть опцію:", reply_markup=reply_markup)
    elif update.callback_query:
        await update.callback_query.message.reply_text("Виберіть опцію:", reply_markup=reply_markup)

# Обробка кнопок
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.message.delete()

    if query.data == 'social':
        keyboard = [
            [InlineKeyboardButton("Instagram🖼️", callback_data='instagram')],
            [InlineKeyboardButton("Facebook👤", callback_data='facebook')],
            [InlineKeyboardButton("Повернутися назад◀", callback_data='main_menu')]
        ]
        await query.message.reply_text("Наші соціальні мережі:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == 'products':
        keyboard = [
            [InlineKeyboardButton("Переглянути товари👕👖👟", callback_data='view_products')],
            [InlineKeyboardButton("OLX", callback_data='olx')],
            [InlineKeyboardButton("Shafa", callback_data='shafa')],
            [InlineKeyboardButton("Повернутися назад◀", callback_data='main_menu')]
        ]
        await query.message.reply_text("Товари:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == 'support':
        keyboard = [
            [InlineKeyboardButton("FAQ⚠", callback_data='faq')],
            [InlineKeyboardButton("Зворотній зв'язок📞", callback_data='contact')],
            [InlineKeyboardButton("Повернутися назад◀", callback_data='main_menu')]
        ]
        await query.message.reply_text("Підтримка:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == 'contest':
        await query.message.reply_photo(
            photo="https://drive.google.com/uc?export=view&id=166ydt8yJ7d55xQKJTm-8tfbVjOf-uk_A",
            caption="Розіграш Светру від бренду Napapijri: [Пост у Instagram](https://www.instagram.com/p/DBMGGlxs7Mm/)",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Повернутися назад◀", callback_data='main_menu')]])
        )

    elif query.data == 'instagram':
        await query.message.reply_photo(
            photo="https://drive.google.com/uc?export=view&id=14tDBbRixB2-Jcu_NaQPErZxUz_07VBsr",
            caption="Наш Instagram: [Casual.0432](https://www.instagram.com/casual.0432/)",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Повернутися назад◀", callback_data='social')]])
        )

    elif query.data == 'facebook':
        await query.message.reply_photo(
            photo="https://drive.google.com/uc?export=view&id=150ZxQ-rQT155M3n1USLcs7pU0nutf3T8",
            caption="Наш Facebook: [Кежуал Вінниця](https://www.facebook.com/profile.php?id=61555261808269)",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Повернутися назад◀", callback_data='social')]])
        )

    elif query.data == 'view_products':
        await query.message.reply_text(
            "Працюємо над цим....",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Повернутися назад◀", callback_data='products')]])
        )

    elif query.data == 'olx':
        await query.message.reply_photo(
            photo="https://drive.google.com/uc?export=view&id=14hjS6RyWKJ4y9oI9igs8BjmHOlKZ-Ge0",
            caption="Оголошення на OLX:\n[Casual Vinnytsya](https://olx.ua)",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Повернутися назад◀", callback_data='products')]])
        )

    elif query.data == 'shafa':
        await query.message.reply_photo(
            photo="https://drive.google.com/uc?export=view&id=14gIxVtNlHkm9HmHwIO9mizAfCgx0zsRV",
            caption="Оголошення на Shafa:\n[CASUAL 0432](https://shafa.ua)",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Повернутися назад◀", callback_data='products')]])
        )

    elif query.data == 'faq':
        await query.message.reply_text(
            "Працюємо над цим....",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Повернутися назад◀", callback_data='support')]])
        )

    elif query.data == 'contact':
        await query.message.reply_text(
            "Є запитання? Звертайтесь: @casual0432support",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Повернутися назад◀", callback_data='support')]])
        )

    elif query.data == 'main_menu':
        await start(update, context)

# Додавання обробників
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

app.run_polling()

