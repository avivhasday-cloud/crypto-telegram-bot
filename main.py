from config import Config
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from functions import *

""""
**************************************************
Function: help_command

returning help message to the user when he type /help 

**************************************************

"""
def help_command(update, context):
    help_message = get_help()
    update.message.reply_text(help_message)
    return


""""
**************************************************
Function: handle_message
Parameters: bot updater

get the user input from the bot updater
get response for that user input
format the response into text and send it 
to the user
if the respose is none send a message to use /help
command

**************************************************
"""
def handle_message(update, context):
    text = str(update.message.text)
    res = get_response(text)
    if isinstance(res, dict):
        formated_response = get_formated_text(res)
    else:
        formated_response = "I don't understand you, please type /help for guidance"
    update.message.reply_text(formated_response)
    
""""
**************************************************
Function: error
return a error message if the bot isnt not working

**************************************************
"""
def error(update, context):
    return f"Update {update} caused error {context.error}"


""""
**************************************************
Function: main

initialize the updater using telegram api key
and use the dispachter
adding handlers so the bot know how to function
when a user write something.
start the bot and waiting for messages

**************************************************
"""
def main():
    # init
    updater = Updater(token=Config.TELEGRAM_API_KEY, use_context=True)
    dispacher = updater.dispatcher

    # add handlers
    dispacher.add_handler(CommandHandler("help", help_command))
    dispacher.add_handler(MessageHandler(Filters.text, handle_message))
    dispacher.add_error_handler(error)

    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    main()


    