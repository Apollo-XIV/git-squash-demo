from random import randint

def ask():
    q = input('''
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
        "Yes",
        "Maybe",
        "No",
        "Bad question"
    ]
    print(
        answers[randint(0,len(answers)-1)]
    )
