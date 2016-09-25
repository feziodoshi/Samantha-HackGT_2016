




    
            
        # is not used by the TerminalAdapter
        # We pass None to this method because the parameter
        bot_input = bot1.get_response(None)
        break
    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
    try:
    x[i]=x[i].replace("\n","")
    x[i]=x[i].strip()
# Create a new instance of a ChatBot
# logging.basicConfig(level=logging.INFO)
# The following loop will execute each time the user enters input
# Uncomment the following line to enable verbose logging
##    
##        "chatterbot.adapters.logic.ClosestMatchAdapter"
##        "chatterbot.adapters.logic.MathematicalEvaluation",
##        "chatterbot.adapters.logic.TimeLogicAdapter",
##        print(bot_input)
##    ],
##    input_adapter="chatterbot.adapters.input.TerminalAdapter",
##    logic_adapters=[
##    output_adapter="chatterbot.adapters.output.TerminalAdapter",
##    storage_adapter="chatterbot.adapters.storage.JsonFileStorageAdapter",
##)
##bot = ChatBot("Terminal",
bot1.set_trainer(ListTrainer)
bot1.train(x[:1000])
bot1=ChatBot("Fenil",filters="chatterbot.filters.RepetitiveResponseFilter",input_adapter="chatterbot.adapters.input.TerminalAdapter",logic_adapter=["chatterboat.adapters.logic.MathematicalEvaluation","chatterbot.adapters.logic.TimeLogicAdapters"],output_adapter="chatterbot.adapters.output.TerminalAdapter",storage_adapter="chatterbot.adapters.storage.JsonFileStorageAdapter")
for i in range(0,len(x)):
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import logging
lines=myFile.read()
myFile=open("bible.txt","r")
print'done'
print("Type something to begin...")
while True:
x=lines.split("\n")