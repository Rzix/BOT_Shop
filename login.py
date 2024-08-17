import telebot
import sqlite3

conn = sqlite3.connect('shop_database.db', check_same_thread=False)
cursor = conn.cursor()

TOKEN = '7244222405:AAFneuARvk-fSOGTIdh9WutkALi-NXtwa0U'
bot = telebot.TeleBot(TOKEN)

user_data = {}

@bot.message_handler(commands=['start', 'login'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, "Are you already registered? (yes/no):")
    bot.register_next_step_handler(msg, process_registration_status_step)

def process_registration_status_step(message):
    chat_id = message.chat.id
    response = message.text.strip().lower()

    if response == 'yes':
        msg = bot.send_message(chat_id, "Please enter your email:")
        bot.register_next_step_handler(msg, process_email_step)
    elif response == 'no':
        msg = bot.send_message(chat_id, "Please enter your desired username for registration:")
        bot.register_next_step_handler(msg, process_registration_username_step)
    else:
        msg = bot.send_message(chat_id, "Invalid response. Please type 'yes' or 'no'.")
        bot.register_next_step_handler(msg, process_registration_status_step)

def process_email_step(message):
    chat_id = message.chat.id
    user_data[chat_id] = {'email': message.text}
    msg = bot.send_message(chat_id, "Please enter your password:")
    bot.register_next_step_handler(msg, process_password_step)

def process_password_step(message):
    chat_id = message.chat.id
    user_data[chat_id]['password'] = message.text

    cursor.execute("SELECT id, role FROM users WHERE email=? AND password=?", 
                   (user_data[chat_id]['email'], user_data[chat_id]['password']))
    user = cursor.fetchone()

    if user:
        user_id, role = user
        user_data[chat_id]['user_id'] = user_id
        user_data[chat_id]['role'] = role

        if role == 'admin':
            bot.send_message(chat_id, "Welcome to the admin panel.")
        else:
            bot.send_message(chat_id, "Welcome to the user panel.")
    else:
        bot.send_message(chat_id, "Invalid credentials. Please try again.")
        send_welcome(message) 

def process_registration_username_step(message):
    chat_id = message.chat.id
    user_data[chat_id] = {'username': message.text}
    msg = bot.send_message(chat_id, "Please enter your email:")
    bot.register_next_step_handler(msg, process_registration_email_step)

def process_registration_email_step(message):
    chat_id = message.chat.id
    user_data[chat_id]['email'] = message.text
    msg = bot.send_message(chat_id, "Please enter a password:")
    bot.register_next_step_handler(msg, process_registration_password_step)

def process_registration_password_step(message):
    chat_id = message.chat.id
    user_data[chat_id]['password'] = message.text
    cursor.execute("INSERT INTO users (username, email, password, role) VALUES (?, ?, ?, ?)", 
                   (user_data[chat_id]['username'], user_data[chat_id]['email'], user_data[chat_id]['password'], 'user'))
    conn.commit()

    bot.send_message(chat_id, "Registration successful! You can now log in with your credentials.")
    send_welcome(message)

# راه‌اندازی ربات
bot.polling()
