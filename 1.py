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
            [InlineKeyboardButton("Чоловічі", callback_data='mens_products')],
            [InlineKeyboardButton("Жіночі", callback_data='womens_products')],
            [InlineKeyboardButton("Повернутися назад◀", callback_data='main_menu')]
        ]
        await query.message.reply_text("Оберіть категорію товарів:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == 'mens_products':
        await query.message.reply_text(
            "Тут буде список чоловічих товарів. (Завантажимо пізніше)",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Повернутися назад◀", callback_data='products')]])
        )

    elif query.data == 'womens_products':
        await query.message.reply_text(
            "Тут буде список жіночих товарів. (Завантажимо пізніше)",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Повернутися назад◀", callback_data='products')]])
        )

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

    elif query.data == 'faq':
        await query.message.reply_text(
            "FAQ:\n\n"
            "1. Чи є продаж без сайтів? - Так, можливо, зв'яжіться з підтримкою.\n\n"
            "2. Чи є повернення товару, якщо не підійшов або з інших причин? - Так, зв'яжіться з підтримкою.\n\n"
            "3. Способи оплати:\n"
            "   - OLX: лише OLX доставка, оплата повної суми, яка заморожується до отримання замовлення.\n"
            "   - Shafa: передоплата на карту або післяплата з мінімальною передоплатою 100 грн. або опція схожа на OLX доставку.",
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
