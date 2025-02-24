from collections import Counter

paragraph = "lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk lmird jk xjubt trmui jx ibndt wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb"
engFreq = {
    'a': 0.0817, 'b': 0.0150, 'c': 0.0278, 'd': 0.0425, 'e': 0.1270, 'f': 0.0223, 'g': 0.0202, 'h': 0.0609, 'i': 0.0697,
    'j': 0.0015, 'k': 0.0077, 'l': 0.0403, 'm': 0.0241, 'n': 0.0675, 'o': 0.0751, 'p': 0.0193, 'q': 0.0010, 'r': 0.0599,
    's': 0.0633, 't': 0.0906, 'u': 0.0276, 'v': 0.0098, 'w': 0.0236, 'x': 0.0015, 'y': 0.0197, 'z': 0.0007
}

letterFreqOfInput = Counter(paragraph)
del letterFreqOfInput[" "]

sorted_counts = sorted(letterFreqOfInput.items(),
                       key=lambda x: x[1], reverse=True)
english_sorted = sorted(engFreq.items(), key=lambda x: x[1], reverse=True)

words = paragraph.split()
transformed_words = []

for word in words:
    new_word = ''
    for char in word:
        sorted_index = next((i for i, item in enumerate(
            sorted_counts) if item[0] == char), None)
        new_char = english_sorted[sorted_index][0] if sorted_index is not None else char
        new_word += new_char
    transformed_words.append(new_word)

new_paragraph = ' '.join(transformed_words)

print("Original Paragraph:\n", paragraph)
print("\nTransformed Paragraph:\n", new_paragraph)

new_paragraph = list(new_paragraph)
for i in range(len(new_paragraph)):
    if new_paragraph[i] == "y":
        new_paragraph[i] = "b"
    elif new_paragraph[i] == "w":
        new_paragraph[i] = "u"
    elif new_paragraph[i] == "f":
        new_paragraph[i] = "p"
    elif new_paragraph[i] == "n":
        new_paragraph[i] = "i"
    elif new_paragraph[i] == "o":
        new_paragraph[i] = "n"
    elif new_paragraph[i] == "i":
        new_paragraph[i] = "o"
    elif new_paragraph[i] == "u":
        new_paragraph[i] = "f"
    elif new_paragraph[i] == "b":
        new_paragraph[i] = "g"
    elif new_paragraph[i] == "g":
        new_paragraph[i] = "y"
    elif new_paragraph[i] == "p":
        new_paragraph[i] = "k"
    elif new_paragraph[i] == "k":
        new_paragraph[i] = "x"
    elif new_paragraph[i] == "x":
        new_paragraph[i] = "q"
    elif new_paragraph[i] == "q":
        new_paragraph[i] = "z"
    elif new_paragraph[i] == "j":
        new_paragraph[i] = "w"

new_paragraph = ''.join(new_paragraph)

print("\nParagraph After Manual Replacements:\n", new_paragraph)
