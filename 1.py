from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = 'YOUR_TOKEN_HERE'
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

    # Соціальні мережі
    if query.data == 'social':
        keyboard = [
            [InlineKeyboardButton("Instagram🖼️", callback_data='instagram')],
            [InlineKeyboardButton("Facebook👤", callback_data='facebook')],
            [InlineKeyboardButton("Повернутися назад◀", callback_data='main_menu')]
        ]
        await query.message.reply_text("Наші соціальні мережі:", reply_markup=InlineKeyboardMarkup(keyboard))

    # Меню товарів
    elif query.data == 'products':
        keyboard = [
            [InlineKeyboardButton("Взуття👟", callback_data='footwear')],
            [InlineKeyboardButton("Штани👖", callback_data='pants')],
            [InlineKeyboardButton("Шорти🩳", callback_data='shorts')],
            [InlineKeyboardButton("Футболки👕", callback_data='tshirts')],
            [InlineKeyboardButton("Кофти🧥", callback_data='hoodies')],
            [InlineKeyboardButton("Куртки🧥", callback_data='jackets')],
            [InlineKeyboardButton("Аксесуари🎒", callback_data='accessories')],
            [InlineKeyboardButton("Повернутися назад◀", callback_data='main_menu')]
        ]
        await query.message.reply_text("Оберіть категорію товарів:", reply_markup=InlineKeyboardMarkup(keyboard))

    # Взуття
    elif query.data == 'footwear':
        keyboard = [
            [InlineKeyboardButton("Чоловіче", callback_data='mens_footwear')],
            [InlineKeyboardButton("Жіноче", callback_data='womens_footwear')],
            [InlineKeyboardButton("Повернутися назад◀", callback_data='products')]
        ]
        await query.message.reply_text("Взуття:", reply_markup=InlineKeyboardMarkup(keyboard))

    # Штани
    elif query.data == 'pants':
        keyboard = [
            [InlineKeyboardButton("Чоловічі", callback_data='mens_pants')],
            [InlineKeyboardButton("Жіночі", callback_data='womens_pants')],
            [InlineKeyboardButton("Повернутися назад◀", callback_data='products')]
        ]
        await query.message.reply_text("Штани:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == 'mens_pants':
        keyboard = [
            [InlineKeyboardButton("Джинси", callback_data='mens_jeans')],
            [InlineKeyboardButton("Спортивні", callback_data='mens_sport_pants')],
            [InlineKeyboardButton("Повернутися назад◀", callback_data='pants')]
        ]
        await query.message.reply_text("Чоловічі штани:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == 'womens_pants':
        keyboard = [
            [InlineKeyboardButton("Джинси", callback_data='womens_jeans')],
            [InlineKeyboardButton("Спортивні", callback_data='womens_sport_pants')],
            [InlineKeyboardButton("Повернутися назад◀", callback_data='pants')]
        ]
        await query.message.reply_text("Жіночі штани:", reply_markup=InlineKeyboardMarkup(keyboard))

    # Шорти
    elif query.data == 'shorts':
        keyboard = [
            [InlineKeyboardButton("Чоловічі", callback_data='mens_shorts')],
            [InlineKeyboardButton("Жіночі", callback_data='womens_shorts')],
            [InlineKeyboardButton("Повернутися назад◀", callback_data='products')]
        ]
        await query.message.reply_text("Шорти:", reply_markup=InlineKeyboardMarkup(keyboard))

    # Футболки
    elif query.data == 'tshirts':
        keyboard = [
            [InlineKeyboardButton("Чоловічі", callback_data='mens_tshirts')],
            [InlineKeyboardButton("Жіночі", callback_data='womens_tshirts')],
            [InlineKeyboardButton("Повернутися назад◀", callback_data='products')]
        ]
        await query.message.reply_text("Футболки:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == 'mens_tshirts':
        keyboard = [
            [InlineKeyboardButton("Звичайні", callback_data='mens_regular_tshirt')],
            [InlineKeyboardButton("Поло", callback_data='mens_polo_tshirt')],
            [InlineKeyboardButton("Термо", callback_data='mens_thermal_tshirt')],
            [InlineKeyboardButton("Повернутися назад◀", callback_data='tshirts')]
        ]
        await query.message.reply_text("Чоловічі футболки:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == 'womens_tshirts':
        keyboard = [
            [InlineKeyboardButton("Звичайні", callback_data='womens_regular_tshirt')],
            [InlineKeyboardButton("Повернутися назад◀", callback_data='tshirts')]
        ]
        await query.message.reply_text("Жіночі футболки:", reply_markup=InlineKeyboardMarkup(keyboard))

    # Кофти
    elif query.data == 'hoodies':
        keyboard = [
            [InlineKeyboardButton("Чоловічі", callback_data='mens_hoodies')],
            [InlineKeyboardButton("Жіночі", callback_data='womens_hoodies')],
            [InlineKeyboardButton("Повернутися назад◀", callback_data='products')]
        ]
        await query.message.reply_text("Кофти:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == 'mens_hoodies':
        keyboard = [
            [InlineKeyboardButton("Худі", callback_data='mens_hoodie')],
            [InlineKeyboardButton("Зіпхуді", callback_data='mens_zip_hoodie')],
            [InlineKeyboardButton("Світшоти", callback_data='mens_sweatshirt')],
            [InlineKeyboardButton("Повернутися назад◀", callback_data='hoodies')]
        ]
        await query.message.reply_text("Чоловічі кофти:", reply_markup=InlineKeyboardMarkup(keyboard))

    # Куртки
    elif query.data == 'jackets':
        keyboard = [
            [InlineKeyboardButton("Чоловічі", callback_data='mens_jackets')],
            [InlineKeyboardButton("Жіночі", callback_data='womens_jackets')],
            [InlineKeyboardButton("Повернутися назад◀", callback_data='products')]
        ]
        await query.message.reply_text("Куртки:", reply_markup=InlineKeyboardMarkup(keyboard))

    # Аксесуари
    elif query.data == 'accessories':
        keyboard = [
            [InlineKeyboardButton("Шапки", callback_data='hats')],
            [InlineKeyboardButton("Сумки", callback_data='bags')],
            [InlineKeyboardButton("Повернутися назад◀", callback_data='products')]
        ]
        await query.message.reply_text("Аксесуари:", reply_markup=InlineKeyboardMarkup(keyboard))

    # Повернення до головного меню
    elif query.data == 'main_menu':
        await start(update, context)

# Додавання обробників
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

app.run_polling()
