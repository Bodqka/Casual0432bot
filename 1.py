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
    await update.message.reply_text("Виберіть опцію:", reply_markup=reply_markup)

# Обробка кнопок
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.message.delete()

    # Меню товарів
    if query.data == 'products':
        keyboard = [
            [InlineKeyboardButton("Взуття👟", callback_data='footwear')],
            [InlineKeyboardButton("Штани👖", callback_data='pants')],
            [InlineKeyboardButton("Шорти🩳", callback_data='shorts')],
            [InlineKeyboardButton("Футболки👕", callback_data='tshirts')],
            [InlineKeyboardButton("Кофти🧥", callback_data='sweatshirts')],
            [InlineKeyboardButton("Куртки🧥", callback_data='jackets')],
            [InlineKeyboardButton("Аксесуари👜", callback_data='accessories')],
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

    # Жіноче взуття
    elif query.data == 'womens_footwear':
        keyboard = [
            [InlineKeyboardButton("Кеди Vans Old Skool", callback_data='vans_old_skool')],
            [InlineKeyboardButton("Повернутися назад◀", callback_data='footwear')]
        ]
        await query.message.reply_text("Жіноче взуття:", reply_markup=InlineKeyboardMarkup(keyboard))

    # Товар: Кеди Vans Old Skool
    elif query.data == 'vans_old_skool':
        description = (
            "Кеди Vans Old Skool\n"
            "- Жіночі\n"
            "- Розмір: 38\n"
            "- Стан: Ідеальний\n"
            "Ціна: 800 грн\n\n"
            "Фото:\n"
            "https://drive.google.com/file/d/1fB8Gvd0DllFqURyldQjKhLvlnyXO6MtM/view\n"
            "https://drive.google.com/file/d/1fFoLVOsuGJOCWP6Qa3KCFEMkGnBjRis1/view\n"
            "https://drive.google.com/file/d/1fJ4mxJj1SbH2FMmOD07MWV04bHXVTOY2/view\n"
            "https://drive.google.com/file/d/1fMaz9pBzddVQutFleqJAp2fXBZacA1cK/view\n"
            "https://drive.google.com/file/d/1fT6gG8BEHXUuGjl-UycwS0JtjS5JCYfQ/view\n"
            "https://drive.google.com/file/d/1fWoa_zPWSyUdJ2E-hEvqXm2l3Vn6i8AG/view\n"
        )
        
        keyboard = [
            [InlineKeyboardButton("Замовити", url="https://t.me/casual0432support")],
            [InlineKeyboardButton("Повернутися назад◀", callback_data='womens_footwear')]
        ]
        await query.message.reply_text(description, reply_markup=InlineKeyboardMarkup(keyboard))

    # Повернення до головного меню
    elif query.data == 'main_menu':
        await start(update, context)

# Додавання обробників
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

app.run_polling()
