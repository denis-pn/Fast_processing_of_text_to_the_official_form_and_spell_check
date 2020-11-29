# pip install pyperclip
import pyperclip
import pymorphy2
from pyaspeller import Word
from tkinter import*
morph = pymorphy2.MorphAnalyzer()
root=Tk()
root.geometry('180x25')
root.resizable(False, False)
# root.overrideredirect(1.5)
root.attributes("-topmost",True)
root.title("  ")
defined = []
coord = []
# text_rep = []
inv = 0

def run():
    global Button
    Button(text="Загрузка", width=30, command=run).pack()
    global inv
    # print(inv)
    coord = []
    root1 = Tk()
    root1.geometry('800x500')
    root1.attributes("-topmost", True)
    a = pyperclip.paste()
    text_one = a.split()
    # print(text_one)
    text_rep = []
    defined = []

    word = []
    text = []
    kav = 0

    i = 0

    while i != len(text_one):
        sim = []
        if text_one[i][len(text_one[i]) - 1] == "." or text_one[i][len(text_one[i]) - 1] == "," or text_one[i][len(text_one[i]) - 1] == ":":
            sim.append(text_one[i][len(text_one[i]) - 1])
        check = Word(text_one[i])
        # print(sim)
        if check.correct == False and text_one[i][0].isupper() == False and text_one[i][0] != "«":
            text.append(check.spellsafe)

            if len(sim) != 0:
                text.append(sim[0])
        else:
            if len(sim) == 0:
                text.append(text_one[i])
            else:
                t = 0
                word = []
                while t != len(text_one[i]) - 1:
                    word.append(text_one[i][t])
                    t += 1

                text.append(''.join(word))
                text.append(sim[0])
        text.append(" ")
        i += 1

    i = 0
    while i != len(text) and len(defined) != 1:

        if text[i].lower() == "я":
            i_1 = i - 1

            while i_1 != i + 3:
                p = morph.parse(text[i_1])[0]
                if p.tag.POS == "VERB" and p.tag.tense == "past":
                    # print(''.join(word_1))
                    defined.append(p.tag.gender)
                i_1 += 1
        i += 1


    if inv == 1:
        if defined[0] == "femn":
            defined.pop()
            defined.append("masc")
        else:
            defined.pop()
            defined.append("femn")
        inv = 0

    i = 0

    while i != len(text):
        # print(text[i][0])

        if len(defined) < 11110:
            # print(text[i])
            # print(text[i][0])
            # print(len(text[i]) - 1)
            if text[i] == "«" or text[i] == '„' or text[i] == '“' or text[i] == '‘':
                kav = 1
                # print()
            elif text[i] == "»" or text[i] == '“' or text[i] == '”' or text[i] == '’':
                kav = 0
            if len(text[i]) >> 1:
                if kav == 1 and (text[i][0] == "«" or text[i][0] == '„' or text[i][0] == '“' or text[i][0] == '‘'):
                    kav = 1
                elif kav == 1 and (text[i][len(text[i]) - 1] == "»" or text[i][len(text[i]) - 1] == '“' or text[i][len(text[i]) - 1] == '”' or text[i][len(text[i]) - 1] == '’'):
                    kav = 0

            p = morph.parse(text[i])[0]
            if p.tag.POS == "VERB" and p.tag.tense == "pres" and kav == 0 and text[i] != None and len(defined) != 0:
                text_rep.append((morph.parse(text[i])[0].inflect({"VERB", 'past', defined[0]}).word))
                coord.append((i, 3))


            elif (text[i] == "я" or text[i] == "Я") and kav == 0 and len(defined) != 0:
                if defined[0] == "femn":
                    if text[i][0].isupper() == False:
                        text_rep.append("она")
                    else:
                        text_rep.append("Она")
                    coord.append((i, 3))
                else:
                    if text[i][0].isupper() == False:
                        text_rep.append("он")
                    else:
                        text_rep.append("Он")
                    coord.append((i, 2))
            elif (text[i] == "меня" or text[i] == "Меня") and kav == 0 and len(defined) != 0:
                if defined[0] == "femn":
                    if text[i][0].isupper() == False:
                        if text[i - 2] == "что" or text[i - 2] == "на" or text[i - 2] == "под" or text[i - 2] == "у" or text[i - 2] == "для":
                            text_rep.append("неё")
                        else:
                            text_rep.append("её")
                    else:
                        if text[i - 1] == "что" or text[i - 1] == "на" or text[i - 1] == "под" or text[i - 1] == "у" or text[i - 2] == "для":
                            text_rep.append("Неё")
                        else:
                            text_rep.append("Её")
                    coord.append((i, 2))
                else:
                    if text[i][0].isupper() == False:
                        if text[i - 1] == "что" or text[i - 1] == "на" or text[i - 1] == "под" or text[i - 1] == "у" or text[i - 2] == "для":
                            text_rep.append("него")
                        else:
                            text_rep.append("его")
                    else:
                        if text[i - 1] == "что" or text[i - 1] == "на" or text[i - 1] == "под" or text[i - 1] == "у" or text[i - 2] == "для":
                            text_rep.append("Него")
                        else:
                            text_rep.append("Его")
                    coord.append((i, 3))
            elif(text[i] == "мне" or text[i] == "Мне") and kav == 0 and len(defined) != 0:
                if defined[0] == "femn":
                    if text[i][0].isupper() == False:
                        text_rep.append("ей")
                    else:
                        text_rep.append("Ей")
                    coord.append((i, 2))
                else:
                    if text[i][0].isupper() == False:
                        text_rep.append("ему")
                    else:
                        text_rep.append("Ему")
                    coord.append((i, 3))

            elif(text[i] == "мои" or text[i] == "Мои" or text[i] == "Моего" or text[i] == "моего") and kav == 0 and len(defined) != 0:
                if defined[0] == "femn":
                    if text[i][0].isupper() == False:
                        text_rep.append("её")
                    else:
                        text_rep.append("Её")
                    coord.append((i, 2))
                else:
                    if text[i][0].isupper() == False:
                        text_rep.append("его")
                    else:
                        text_rep.append("Его")
                    coord.append((i, 3))

            elif (text[i] == "мной" or text[i] == "Мной") and kav == 0 and len(defined) != 0:
                if defined[0] == "femn":
                    if text[i][0].isupper() == False:
                        text_rep.append("ней")
                    else:
                        text_rep.append("Ней")
                    coord.append((i, 2))
                else:
                    if text[i][0].isupper() == False:
                        text_rep.append("ним")
                    else:
                        text_rep.append("Ним")
                    coord.append((i, 3))
            elif (text[i] == "мы" or text[i] == "Мы") and kav == 0:
                # print(text[i])
                if text[i][0].isupper() == False:
                    text_rep.append("они")
                    coord.append((i, 3))
                else:
                    text_rep.append("Они")
                    coord.append((i, 3))
            elif (text[i] == "нас" or text[i] == "Нас") and kav == 0:
                if text[i][0].isupper() == False:
                    text_rep.append("их")
                    coord.append((i, 3))
                else:
                    text_rep.append("Их")
                    coord.append((i, 2))
            else:
                text_rep.append(text[i])
        i += 1



    tx1 = Text(root1, width=100, height=25)
    if len(coord) != 0:
        # print(coord)
        i = 0
        # tx1 = Text(root1)
        tx1.tag_config('tag_red_text', foreground='red')
        # print(len(text_rep))
        while i != len(text_rep):
            p = 0
            i_1 = 0
            while i_1 != len(coord):
                if i == coord[i_1][0]:
                    p = 1
                i_1 += 1

            if p == 1:
                tx1.insert("end", ''.join(text_rep[i]), 'tag_red_text')
            elif text_rep[i] == None:
                tx1.insert("end", text_one[i])
            else:
                # print(text_rep[i])
                tx1.insert("end", ''.join(text_rep[i]))
            i += 1
        tx1.pack()
    else:
        tx1.insert("end", "Варианты обработки текста не найдены ")
        tx1.pack()

    Button(root1, text="Все верно", width=50, command=lambda root1=root1, text_rep=text_rep:enter(root1, text_rep)).pack()
    Button(root1, text="Изменить род", width=50, command=lambda root1=root1, a=a:rod(root1, a)).pack()

def rod(root1, a):
    global inv
    pyperclip.copy(a)
    root1.destroy()
    inv = 1
    run()

def enter(root1, text_rep):
    # print(''.join(text_rep))
    root1.destroy()
    pyperclip.copy(''.join(text_rep))




Button(text="Обработка текста", width=30, command=run).pack()
root.mainloop()