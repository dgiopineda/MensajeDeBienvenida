from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Token de tu bot (lo obtuviste del BotFather)
TOKEN = '7590055696:AAE0iv1D3H6YBluMXMrFCFKwEkYVF50MH0w'

# Función de inicio que responde con un mensaje de bienvenida y envía una imagen
async def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    await update.message.reply_text(f"¡Hola, {user.first_name}! Bienvenido a la Familia ALFA")
    
    # Enviar imagen de bienvenida
    with open('Banner 4 Bienvenido.jpg', 'rb') as photo:
        await update.message.reply_photo(photo=photo, caption="¡Nos alegra que te unas a nosotros!")

# Función para manejar los nuevos miembros del grupo
async def new_member(update: Update, context: CallbackContext) -> None:
    for member in update.message.new_chat_members:
        await update.message.reply_text(f"¡Bienvenido, {member.full_name}! FAMILIA ALFA.")
        
        # Enviar imagen de bienvenida para nuevos miembros
        with open(r'C:\Users\10 Spring Creators\Desktop\Bots\Banner 4 Bienvenido.jpg', 'rb') as photo:
            await update.message.reply_photo(photo=photo, caption="¡FAMILIA-FUERZA-VICTORIA!")

# Configuración principal del bot
def main() -> None:
    application = Application.builder().token(TOKEN).build()
    
    # Maneja el comando /start
    application.add_handler(CommandHandler("start", start))
    
    # Maneja los nuevos miembros en el grupo
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, new_member))
    
    # Comienza el bot
    application.run_polling()

if __name__ == '__main__':
    main()
