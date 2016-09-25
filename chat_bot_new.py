from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import logging
print'done'

myFile=open("notebook.txt","r")
lines=myFile.read()
x=lines.split(".")
for i in range(0,len(x)):
    x[i]=x[i].strip()
    x[i]=x[i].replace("\n","")
    
# Uncomment the following line to enable verbose logging
# logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot
##bot = ChatBot("Terminal",
##    storage_adapter="chatterbot.adapters.storage.JsonFileStorageAdapter",
##    logic_adapters=[
##        "chatterbot.adapters.logic.MathematicalEvaluation",
##        "chatterbot.adapters.logic.TimeLogicAdapter",
##        "chatterbot.adapters.logic.ClosestMatchAdapter"
##    ],
##    input_adapter="chatterbot.adapters.input.TerminalAdapter",
##    output_adapter="chatterbot.adapters.output.TerminalAdapter",
##    
##)
bot=ChatBot("Fenil",filters="chatterbot.filters.RepetitiveResponseFilter",input_adapter="chatterbot.adapters.input.TerminalAdapter",logic_adapter=["chatterboat.adapters.logic.MathematicalEvaluation","chatterbot.adapters.logic.TimeLogicAdapters"],output_adapter="chatterbot.adapters.output.TerminalAdapter",storage_adapter="chatterbot.adapters.storage.JsonFileStorageAdapter")
bot.set_trainer(ListTrainer)
bot.train(x[:20])
print("Type something to begin...")


# The following loop will execute each time the user enters input
while True:
    try:
        # We pass None to this method because the parameter
        # is not used by the TerminalAdapter
        bot_input = bot.get_response(None)
##        print(bot_input)
            

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
