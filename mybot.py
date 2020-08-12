# http://t.me/ipmpavg_bot
#setup:
#1.pip install pyTelegramBotAPI
#2.sudo apt install snmp
#3.check command on colsole with your server: snmpwalk -v3 -l authNoPriv -u visadm -a SHA -A "Admin123" 94.125.123.161 .1.3.6.1.4.1.2021.10.1.3.1

import os
import time
import telebot

bot = telebot.TeleBot('1202846575:AAFaHagBxbXOOv28u7sejdXM639sOXFShNU')

@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Please input server (example 94.125.123.160)')
    bot.register_next_step_handler(sent, cores)

def cores(message):
    global server
    server = (message.text)
    sent2 = bot.send_message(message.chat.id, 'Input number of cores')
    bot.register_next_step_handler(sent2, botstarted)

def botstarted(message):
    global core
    global bye
    core = (message.text)
    cores = float(core)
    bot.send_message(message.chat.id, 'Check started, if load average more then number of cores you get Warning message ')
    while (True):
        b = os.popen('snmpwalk -v3 -l authNoPriv -u visadm -a SHA -A "Admin123" ' + server + ' .1.3.6.1.4.1.2021.10.1.3.1').read()
        d = (b[39:43])
        c = float(b[39:43])
        if c > cores:
            bot.send_message(message.chat.id, 'Warning, huge load average: ' + d)
        print(c)
        time.sleep(10)

@bot.message_handler(commands=["stop"])
def cmd_reset(message):
    bot.send_message(message.chat.id, "bye!")



#RUN
bot.polling(none_stop=True)
