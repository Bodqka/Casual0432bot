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

# Додавання товарів до розділу «Жіночі»
async def womens_products(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Кеди Vans", url='https://t.me/casual0432/4')],
        [InlineKeyboardButton("Футболка FSBN", url='https://t.me/casual0432/62')],
        [InlineKeyboardButton("Топ Adidas originals", url='https://t.me/casual0432/65')],
        [InlineKeyboardButton("Футболка The North Face", url='https://t.me/casual0432/68')],
        [InlineKeyboardButton("Футболка The North Face", url='https://t.me/casual0432/93')],
        [InlineKeyboardButton("Nike шорти", url='https://t.me/casual0432/131')],
        [InlineKeyboardButton("Жіночі штани", url='https://t.me/casual0432/160')],
        [InlineKeyboardButton("Джинси Levi's San Francisco", url='https://t.me/casual0432/163')],
        [InlineKeyboardButton("Гольф Ralph Lauren", url='https://t.me/casual0432/187')],
        [InlineKeyboardButton("Футболка Fila", url='https://t.me/casual0432/276')],
        [InlineKeyboardButton("Куртка Karrimor", url='https://t.me/casual0432/303')],
        [InlineKeyboardButton("Adidas originals укорочена футболка", url='https://t.me/casual0432/467')],
        [InlineKeyboardButton("George худі", url='https://t.me/casual0432/499')],
        [InlineKeyboardButton("Повернутися назад◀", callback_data='products')]
    ]
    await update.callback_query.message.reply_text("Жіночі👩 товари📦:", reply_markup=InlineKeyboardMarkup(keyboard))

# Додавання товарів до розділу «Чоловічі»
async def mens_products(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Штани Ellesse", url='https://t.me/casual0432/10')],
        [InlineKeyboardButton("Штани Adidas Performance Essentials", url='https://t.me/casual0432/15')],
        [InlineKeyboardButton("Джинси Levi's", url='https://t.me/casual0432/19')],
        [InlineKeyboardButton("Футболка Lyle and Scott", url='https://t.me/casual0432/23')],
        [InlineKeyboardButton("Шорти Dickies", url='https://t.me/casual0432/27')],
        [InlineKeyboardButton("Повернутися назад◀", callback_data='products')]
    ]
    await update.callback_query.message.reply_text("Чоловічі🧔 товари📦:", reply_markup=InlineKeyboardMarkup(keyboard))

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
            [InlineKeyboardButton("Чоловічі🧔", callback_data='mens_products')],
            [InlineKeyboardButton("Жіночі👩", callback_data='womens_products')],
            [InlineKeyboardButton("Повернутися назад◀", callback_data='main_menu')]
        ]
        await query.message.reply_text("Оберіть категорію товарів:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == 'mens_products':
        await mens_products(update, context)

    elif query.data == 'womens_products':
        await womens_products(update, context)

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
        await query.message.reply_photo(
            photo="https://drive.google.com/uc?id=1gzRzbx3Ji2nK6CL8cWb2ZKEmholIIIX3",
            caption="Є запитання? Звертайтесь: @casual0432support",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Повернутися назад◀", callback_data='support')]])
        )

    elif query.data == 'main_menu':
        await start(update, context)

# Додавання обробників
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

app.run_polling()
