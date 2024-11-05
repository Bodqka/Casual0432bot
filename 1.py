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
            [InlineKeyboardButton("Повернутися назад◀", callback_data='main_menu')]
        ]
        await query.message.reply_text("Оберіть категорію товарів:", reply_markup=InlineKeyboardMarkup(keyboard))

    # Взуття
    elif query.data == 'footwear':
        keyboard = [
            [InlineKeyboardButton("Кеди Vans Old Skool", callback_data='vans_old_skool')],
            [InlineKeyboardButton("Повернутися назад◀", callback_data='products')]
        ]
        await query.message.reply_text("Взуття:", reply_markup=InlineKeyboardMarkup(keyboard))

    # Кеди Vans Old Skool
    elif query.data == 'vans_old_skool':
        description = (
            "Кеди Vans Old Skool з принтом\n"
            "- 38 Розмір\n"
            "- Стан: Ідеальний\n"
            "Ціна: 800 грн\n\n"
            "Фото:\n"
            "https://images.shafastatic.net/-435140327\n"
            "https://images.shafastatic.net/-435140325\n"
            "https://images.shafastatic.net/-435140332\n"
            "https://images.shafastatic.net/-435140322\n"
            "https://images.shafastatic.net/-435140320\n"
            "https://images.shafastatic.net/-435140317\n"
        )
        
        keyboard = [
            [InlineKeyboardButton("Замовити", url="https://t.me/casual0432support")],
            [InlineKeyboardButton("Повернутися назад◀", callback_data='footwear')]
        ]
        await query.message.reply_text(description, reply_markup=InlineKeyboardMarkup(keyboard))

    # Повернення до головного меню
    elif query.data == 'main_menu':
        await start(update, context)

# Додавання обробників
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

app.run_polling()
