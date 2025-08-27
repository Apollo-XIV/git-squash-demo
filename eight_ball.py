from random import randint

def ask():
    _ = input('''
         ____
    ,dP9CGG88@b,
  ,IP  _   Y888@@b,
 dIi  (_)   G8888@b
dCII  (_)   G8888@@b
GCCIi     ,GG8888@@@
GGCCCCCCCGGG88888@@@
GGGGCCCGGGG88888@@@@...
Y8GGGGGG8888888@@@@P.....
 Y88888888888@@@@@P......
 `Y8888888@@@@@@@P'......
    `@@@@@@@@@P'.......
        """"........

What do you ask the 8 ball?
''')
    answers = [
        "Did you really need me for that?",
        "Yes, but only if you write a 10-page report first.",
        "No, but nice try.",
        "Please hold… your answer is important to us.",
        "Error: Answer service unavailable.",
        "Outlook good… for literally anything else.",
        "Ask again later, I’m busy.",
        "Sure, if you believe hard enough.",
        "Signs point to… meh.",
        "Reply hazy, please try turning it off and on again.",
        "Most likely… but I wouldn’t bet on it.",
        "Better not tell you now, it’ll ruin the surprise.",
        "Cannot predict now, coffee levels are too low.",
        "Very doubtful, but keep dreaming.",
        "My reply is no, with extreme prejudice.",
        "Yes – definitely… not.",
        "Without a doubt… that you’ll ask again.",
        "It is certain… that I’m being unhelpful.",
        "You may rely on it… but you probably shouldn’t.",
        "As I see it… you’re still waiting for a real answer."
    ]
    print(
        answers[randint(0,len(answers)-1)]
    )
