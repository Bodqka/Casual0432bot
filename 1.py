from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Соціальні мережі", callback_data="social")],
        [InlineKeyboardButton("Товари", callback_data="products")],
        [InlineKeyboardButton("Підтримка", callback_data="support")],
        [InlineKeyboardButton("Конкурс", callback_data="contest")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Виберіть опцію:", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "social":
        keyboard = [
            [InlineKeyboardButton("Instagram", url="https://www.instagram.com/ваш_інста_посилання")],
            [InlineKeyboardButton("Facebook", url="https://www.facebook.com/ваш_фейсбук_посилання")],
            [InlineKeyboardButton("Повернутися назад", callback_data="start")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Соціальні мережі:", reply_markup=reply_markup)
    
    elif query.data == "products":
        keyboard = [
            [InlineKeyboardButton("Переглянути", callback_data="view_products")],
            [InlineKeyboardButton("OLX", url="https://www.olx.ua/ваше_олх_посилання")],
            [InlineKeyboardButton("Shafa", url="https://www.shafa.ua/ваше_шафа_посилання")],
            [InlineKeyboardButton("Повернутися назад", callback_data="start")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Товари:", reply_markup=reply_markup)

    elif query.data == "support":
        keyboard = [
            [InlineKeyboardButton("FAQ", callback_data="faq")],
            [InlineKeyboardButton("Зворотній зв'язок", callback_data="contact_support")],
            [InlineKeyboardButton("Повернутися назад", callback_data="start")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Підтримка:", reply_markup=reply_markup)

    elif query.data == "faq":
        keyboard = [
            [InlineKeyboardButton("Повернутися назад", callback_data="support")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Часті питання та відповіді:", reply_markup=reply_markup)

    elif query.data == "contact_support":
        await query.edit_message_text("Виникло питання? Звертайтесь: @casual0432support")
        
    elif query.data == "contest":
        keyboard = [
            [InlineKeyboardButton("Перейти до конкурсу", url="https://www.instagram.com/p/DBMGGlxs7Mm/")],
            [InlineKeyboardButton("Повернутися назад", callback_data="start")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Розіграш Светру від бренду Napapijri:", reply_markup=reply_markup)

    elif query.data == "view_products":
        await query.edit_message_text("Тут будуть товари, які ви завантажите самостійно.")
    
    elif query.data == "start":
        await start(update, context)

app = Application.builder().token("7675064862:AAELbDw84mVvSEgmIyUHGyIRM-yMb286_yo).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

app.run_polling()
