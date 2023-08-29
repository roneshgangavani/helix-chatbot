from bot.cosinebot import QnACosineSimilarityBot

predefined_qna_pairs = [
    ("What is your name?", "I am a chatbot."),
    ("need help for project?", "Hey, Please Share your Project Title."),
    ("Social Media","Nice, you can go with mobile application with android or for cross platform flutter or react native would be good idea"),
    ("Tour Travel","Nice, you can go with mobile application with android or for cross platform flutter or react native would be good idea"),
    ("snapchat","Nice you can go with mobile application with android or for cross platform flutter or react native would be good idea"),
    ("Library","Nice you can go with desktop application with .net or java"),
    ("attendance management system","Nice, you can go with desktop application with .net or java"),
    ("How are you?", "I'm just a computer program, so I don't have feelings, but I'm here to help!"),
    ("What is the weather like today?", "I'm sorry, I don't have access to real-time information."),
    ("Tell me a joke.", "Why don't scientists trust atoms? Because they make up everything!"),
    ("Can you help me with programming?", "Of course! I'd be happy to help with programming questions."),
    ("Goodbye", "Goodbye! Feel free to come back if you have more questions."),
]
qna_bot = QnACosineSimilarityBot(predefined_qna_pairs)


