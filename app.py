from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def menu(update:Update, context:CallbackContext)-> None:
    keyboard =[keyboardButton("Listas de productos")],
    [KeyboardButton("Mapa")],
    [KeyboardButton("Horarios")],
    [KeyboardButton("N")],
    [KeyboardButton("Servicios")],
    [KeyboardButton("Denuncia")],
    
    menu_choices = ReplyKeyboardMarkup(keyboard)
    await context.bot.send_message(chat_id=update.message.chat_id, text = "Opciones", reply_markup=menu_choices)

app = ApplicationBuilder().token("8462445576:AAHvK40v1bSi5twBDfU7oKlgxDWHXEuW-bY").build()

app.add_handler(CommandHandler("menu",menu))
app.add_handler(CommandHandler("hello", hello))

app.run_polling()
