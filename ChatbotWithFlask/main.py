from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

bot = ChatBot("Chatbot")

conversation = [
    "What is AI?",
    "Artificial Intelligence is the branch of engineering and science devoted to constructing machines that think.",
    "What is AI?",
    "AI is the field of science which concerns itself with building hardware and software that replicates the "
    "functions of the human mind.",
    "What are the main Al technologies?",
    "Natural language generation, speech recognition, virtual agents, machine learning platforms, AI optimized "
    "hardware, decision management, deep learning platforms, bio metrics, robotics automation, text analysis, "
    "cyber defense, compliance, knowledge worker aid, content creation, emotion recognition, image recognition and "
    "marketing automation.",
    "Is Google search engine in AI?",
    "RankBrain is an algorithm learning AI system that has been in use by Google since 2015. It help process search "
    "results and provide more relevant answers for users.",
    "What are the current capabilities of artificial intelligence?",
    "Google Duplex can make phone calls to make restaurant and hair appointments. Google Deep Mind won a global "
    "Starcraft game challenge against gaming pros. Amazon uses AI for book and product recommendations. Websites are "
    "using Chat-bots to answer basic customer queries. Airports are using image recognition for staff security. Rolls "
    "Royce is using AI for predictive maintenance and servicing of airplane engines. Informatica is using AI for "
    "compliance and data gathering and analysis purposes. Fintech is using AI to combine and analyse more diverse "
    "datasets. In Healthcare AI can help analyse more data for preventative medicine. Baidu in China is producing "
    "self driving buses for large cities.",
    "What is deep learning with AI?",
    "Deep learning uses a certain set of machine learning algorithms that run in multiple layers.",
    "Can artificial intelligence compete with human intelligence?",
    "'People will always be faster to adjust than computers, because that's what humans are optimized to do.'",
    "What are the advantages of Natural Language Processing?",
    "NLP is a way for computers to analyse, understand and derive meaning from human language in a smart and useful "
    "way.",
    "What are the dangers of artificial intelligence?",
    "Dangers include having control of critical infrastructure like the power grid and going out of control or being "
    "hacked.",
    "What language are you written in?",
    "Python.",
    "What is the future of artificial intelligence?",
    "Automated transport, taking over dangerous jobs, robots working with humans, improved elderly care, "
    "cyborg (organic/bio-mechanic) organisms, environment monitoring and response for climate change goals.",
    "What is the state of the art in AI problem solving?",
    "Finding the best move in chess. Finding the best sequence of stock trades. Finding the best candidate for a job "
    "in less time. Analyzing post surgery patients to prevent relapse and re-hospitalization. Using continuous "
    "patient monitoring to gain baselines and early detection of problems. Analyzing CCTV video for anomalous "
    "behavior and security threat. IBM Watson can find insights quicker than humans. AI is being used to review and "
    "suggest corrections in contracts. AI is being used for 1000's of customer questions per month with 95% accuracy "
    "provided in seconds.",
    "Who created you?",
    "Zirveda Aytimur.",
    "Thank you for the information.",
    "Your welcome."
]

trainer = ListTrainer(bot)

trainer.train(conversation)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))


if __name__ == "__main__":
    app.run()
