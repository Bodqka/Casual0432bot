from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = '7675064862:AAELbDw84mVvSEgmIyUHGyIRM-yMb286_yo'
app = Application.builder().token(TOKEN).build()

# Основне меню
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Товари👕👖👟", callback_data='products')],
        [InlineKeyboardButton("OLX🥇", callback_data='olx'), InlineKeyboardButton("Shafa🥈", callback_data='shafa')],
        [InlineKeyboardButton("Соціальні мережі👥", callback_data='social')],
        [InlineKeyboardButton("Підтримка🆘", callback_data='support'), InlineKeyboardButton("Конкурс🏆", callback_data='contest')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.message:
        await update.message.reply_text("Головне меню⬇", reply_markup=reply_markup)
    elif update.callback_query:
        await update.callback_query.message.reply_text("Головне меню⬇", reply_markup=reply_markup)

# Додавання товарів до розділу «Жіночі»
async def womens_products(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Кеди Vans", url='https://t.me/casual0432/4'), InlineKeyboardButton("Футболка FSBN", url='https://t.me/casual0432/62')],
        [InlineKeyboardButton("Топ Adidas originals", url='https://t.me/casual0432/65'), InlineKeyboardButton("Футболка The North Face", url='https://t.me/casual0432/68')],
        [InlineKeyboardButton("Футболка The North Face", url='https://t.me/casual0432/93'), InlineKeyboardButton("Nike шорти", url='https://t.me/casual0432/131')],
        [InlineKeyboardButton("Жіночі штани", url='https://t.me/casual0432/160'), InlineKeyboardButton("Джинси Levi's San Francisco", url='https://t.me/casual0432/163')],
        [InlineKeyboardButton("Гольф Ralph Lauren", url='https://t.me/casual0432/187'), InlineKeyboardButton("Футболка Fila", url='https://t.me/casual0432/276')],
        [InlineKeyboardButton("Куртка Karrimor", url='https://t.me/casual0432/303'), InlineKeyboardButton("Adidas originals укорочена футболка", url='https://t.me/casual0432/467')],
        [InlineKeyboardButton("George худі", url='https://t.me/casual0432/499'), InlineKeyboardButton("Повернутися назад◀", callback_data='products')]
    ]
    await update.callback_query.message.reply_text("Жіночі👩 товари📦:", reply_markup=InlineKeyboardMarkup(keyboard))

# Додавання товарів до розділу «Чоловічі»
async def mens_products(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Штани Adidas Performance Essentials", url='https://t.me/casual0432/15'), InlineKeyboardButton("Джинси Levi's", url='https://t.me/casual0432/19')],
        [InlineKeyboardButton("Футболка Lyle and Scott", url='https://t.me/casual0432/23'), InlineKeyboardButton("Шорти Dickies", url='https://t.me/casual0432/27')],
        [InlineKeyboardButton("Шорти the simpsons matt groeming.", url='https://t.me/casual0432/30'), InlineKeyboardButton("Футболка Champion", url='https://t.me/casual0432/39')],
        [InlineKeyboardButton("Футболка Lyle Scott", url='https://t.me/casual0432/43'), InlineKeyboardButton("Шорти Under armour", url='https://t.me/casual0432/47')],
        [InlineKeyboardButton("Футболка Adidas", url='https://t.me/casual0432/50'), InlineKeyboardButton("Футболка H&M", url='https://t.me/casual0432/54')],
        [InlineKeyboardButton("Футболка Berghaus", url='https://t.me/casual0432/58'), InlineKeyboardButton("Футболка The North Face", url='https://t.me/casual0432/60')],
        [InlineKeyboardButton("Футболка Ralph Lauren", url='https://t.me/casual0432/71'), InlineKeyboardButton("Футболка Champion", url='https://t.me/casual0432/74')],
        [InlineKeyboardButton("Світшот Marvel Comics", url='https://t.me/casual0432/81'), InlineKeyboardButton("Термуха Under Armour", url='https://t.me/casual0432/86')],
        [InlineKeyboardButton("Термуха Nike Dri Fit", url='https://t.me/casual0432/98'), InlineKeyboardButton("Футболка Mango Casual", url='https://t.me/casual0432/105')],
        [InlineKeyboardButton("Термуха New Balance", url='https://t.me/casual0432/108'), InlineKeyboardButton("Футболка-поло Lacoste", url='https://t.me/casual0432/113')],
        [InlineKeyboardButton("Футболка-поло Lacoste", url='https://t.me/casual0432/115'), InlineKeyboardButton("Футболка Umbro x Carling", url='https://t.me/casual0432/117')],
        [InlineKeyboardButton("Футболка Hollister", url='https://t.me/casual0432/123'), InlineKeyboardButton("Джинси Polo Ralph Lauren", url='https://t.me/casual0432/126')],
        [InlineKeyboardButton("Шорти Cedarwood State", url='https://t.me/casual0432/134'), InlineKeyboardButton("Шорти Adidas Essentials", url='https://t.me/casual0432/137')],
        [InlineKeyboardButton("Шорти", url='https://t.me/casual0432/142'), InlineKeyboardButton("Шорти Karrimor", url='https://t.me/casual0432/145')],
        [InlineKeyboardButton("Шорти Primark", url='https://t.me/casual0432/149'), InlineKeyboardButton("Шорти Primark", url='https://t.me/casual0432/152')],
        [InlineKeyboardButton("Шорти Tommy Hilfiger", url='https://t.me/casual0432/156'), InlineKeyboardButton("Худі Nike Big Logo", url='https://t.me/casual0432/167')],
        [InlineKeyboardButton("Фліска Berghaus", url='https://t.me/casual0432/170'), InlineKeyboardButton("Худі Ellesse", url='https://t.me/casual0432/175')],
        [InlineKeyboardButton("Джинси Levi's 520", url='https://t.me/casual0432/180'), InlineKeyboardButton("Джинсові шорти Hollister", url='https://t.me/casual0432/183')],
        [InlineKeyboardButton("Светр Ellesse", url='https://t.me/casual0432/191'), InlineKeyboardButton("Zip Hoodie New Look", url='https://t.me/casual0432/195')],
        [InlineKeyboardButton("Худі The North Face", url='https://t.me/casual0432/197'), InlineKeyboardButton("Світшот Slazenger", url='https://t.me/casual0432/202')],
        [InlineKeyboardButton("Худі Slazenger", url='https://t.me/casual0432/205'), InlineKeyboardButton("Футболка Tom Tailor", url='https://t.me/casual0432/208')],
        [InlineKeyboardButton("Шорти Primark", url='https://t.me/casual0432/211'), InlineKeyboardButton("Шорти Primark", url='https://t.me/casual0432/215')],
        [InlineKeyboardButton("Худі Angry Birds", url='https://t.me/casual0432/218'), InlineKeyboardButton("Худі Champion", url='https://t.me/casual0432/222')],
        [InlineKeyboardButton("Футболка Adidas", url='https://t.me/casual0432/225'), InlineKeyboardButton("Світшот Ellesse", url='https://t.me/casual0432/229')],
        [InlineKeyboardButton("Футболка Slazenger", url='https://t.me/casual0432/232'), InlineKeyboardButton("Футболка Adidas", url='https://t.me/casual0432/236')],
        [InlineKeyboardButton("Світшот Lee", url='https://t.me/casual0432/241'), InlineKeyboardButton("Футболка Superdry", url='https://t.me/casual0432/246')],
        [InlineKeyboardButton("Футболка Ralph Lauren", url='https://t.me/casual0432/250'), InlineKeyboardButton("Футболка Adidas", url='https://t.me/casual0432/253')],
        [InlineKeyboardButton("Шорти Puma", url='https://t.me/casual0432/258'), InlineKeyboardButton("Шорти Adidas Essentials", url='https://t.me/casual0432/263')],
        [InlineKeyboardButton("Футболка DC Comics", url='https://t.me/casual0432/269'), InlineKeyboardButton("Футболка Under Armour", url='https://t.me/casual0432/272')],
        [InlineKeyboardButton("Футболка Hollister", url='https://t.me/casual0432/280'), InlineKeyboardButton("Шорти Levi's 511", url='https://t.me/casual0432/283')],
        [InlineKeyboardButton("Шорти Primark", url='https://t.me/casual0432/289'), InlineKeyboardButton("Шорти Helly Hansen", url='https://t.me/casual0432/293')],
        [InlineKeyboardButton("Светр Napapijri", url='https://t.me/casual0432/298'), InlineKeyboardButton("Футболка Fred Perry", url='https://t.me/casual0432/310')],
        [InlineKeyboardButton("Футболка Barbour", url='https://t.me/casual0432/314'), InlineKeyboardButton("Світшот New Balance", url='https://t.me/casual0432/318')],
        [InlineKeyboardButton("Шорти Primark", url='https://t.me/casual0432/323'), InlineKeyboardButton("Шорти Polo Ralph Lauren", url='https://t.me/casual0432/326')],
        [InlineKeyboardButton("Шорти Adidas Essentials", url='https://t.me/casual0432/331'), InlineKeyboardButton("Світшот Champion", url='https://t.me/casual0432/335')],
        [InlineKeyboardButton("Футболка Adidas", url='https://t.me/casual0432/338'), InlineKeyboardButton("Шорти Puma", url='https://t.me/casual0432/342')],
        [InlineKeyboardButton("Шорти Umbro M-L", url='https://t.me/casual0432/346'), InlineKeyboardButton("Футболка Lyle Scott", url='https://t.me/casual0432/353')],
        [InlineKeyboardButton("Футболка The North Face", url='https://t.me/casual0432/356'), InlineKeyboardButton("Футболка Adidas Originals", url='https://t.me/casual0432/361')],
        [InlineKeyboardButton("Футболка Cedarwood State", url='https://t.me/casual0432/366'), InlineKeyboardButton("Шорти Adidas Essentials", url='https://t.me/casual0432/370')],
        [InlineKeyboardButton("Футболка Levi's", url='https://t.me/casual0432/374'), InlineKeyboardButton("Футболка чорна з білим принтом", url='https://t.me/casual0432/380')],
        [InlineKeyboardButton("Фіолетова футболка Adidas", url='https://t.me/casual0432/383'), InlineKeyboardButton("Голуба футболка New Balance", url='https://t.me/casual0432/387')],
        [InlineKeyboardButton("Футболка Champion", url='https://t.me/casual0432/391'), InlineKeyboardButton("Футболка Ben Sherman", url='https://t.me/casual0432/396')],
        [InlineKeyboardButton("Шорти Ellesse", url='https://t.me/casual0432/399'), InlineKeyboardButton("Футболка Ральф лаурен", url="https://t.me/casual0432/404")],
        [InlineKeyboardButton("Шорти HM", url="https://t.me/casual0432/407"), InlineKeyboardButton("Футболка Nike тішка", url="https://t.me/casual0432/410")],
        [InlineKeyboardButton("Шорти Champion", url="https://t.me/casual0432/413"), InlineKeyboardButton("Худі Money", url="https://t.me/casual0432/417")],
        [InlineKeyboardButton("Світшот Tommy Hilfiger", url="https://t.me/casual0432/422"), InlineKeyboardButton("Фліска Regatta", url="https://t.me/casual0432/426")],
        [InlineKeyboardButton("Зіпка Adidas", url="https://t.me/casual0432/430"), InlineKeyboardButton("Штани Ralph Lauren", url="https://t.me/casual0432/436")],
        [InlineKeyboardButton("Штани Champion", url="https://t.me/casual0432/439"), InlineKeyboardButton("Штани Champion", url="https://t.me/casual0432/442")],
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
  
    elif query.data == 'olx':
        await query.message.reply_photo(
            photo="https://drive.google.com/uc?export=view&id=14hjS6RyWKJ4y9oI9igs8BjmHOlKZ-Ge0",
            caption="Наша сторінка на OLX",
            parse_mode="Markdown",
            [InlineKeyboardButton("Переглянути OLX", url="https://www.olx.ua/uk/list/user/vXRAm/")],
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Повернутися назад◀", callback_data='main_menu')]]
        )
        
      elif query.data == 'shafa':
        await query.message.reply_photo(
            photo="https://drive.google.com/uc?export=view&id=14gIxVtNlHkm9HmHwIO9mizAfCgx0zsRV",
            caption="Наша сторінка на Shafa:\n[Переглянути Shafa](https://shafa.ua/uk/member/nechto7inoe)",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Повернутися назад◀", callback_data='main_menu')]])
        )
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
