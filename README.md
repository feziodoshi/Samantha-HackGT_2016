# Samantha

Romantic conversational chatbot using python and [chatterbot](https://github.com/gunthercox/ChatterBot).
Made at [HackGT 2016](https://hackgt.com). More info at [Devpost](http://devpost.com/software/trumpit-q37awp).


### Chatterbot Installation

This package can be installed from [PyPi](https://pypi.python.org/pypi/ChatterBot) by running:

```
pip install chatterbot
```

### Training data

Chatterbot comes with a data utility module that can be used to train chat bots.
At the moment there is three languages, English, Spanish and Portuguese training data in this module. Contributions
of additional training data or training data in other languages would be greatly
appreciated. Take a look at the data files in the
[chatterbot/corpus](https://github.com/gunthercox/ChatterBot/tree/master/chatterbot/corpus)
directory if you are interested in contributing.

```
# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

# Train based on english greetings corpus
chatbot.train("chatterbot.corpus.english.greetings")

# Train based on the english conversations corpus
chatbot.train("chatterbot.corpus.english.conversations")
```

**Corpus contributions are welcome! Please make a pull request.**

### Chatterbot [Documentation](http://chatterbot.readthedocs.io/)

View the [documentation](http://chatterbot.readthedocs.io/)
for ChatterBot on Read the Docs.

## TO-DO

- [ ] Add human conversation corpus
- [ ] Make one chatbot talk to another
