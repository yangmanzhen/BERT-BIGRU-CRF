
path = r'data/dev'
res_path = r'data/hi'

f = open(path, encoding='utf-8')
f1 = open(res_path, 'w+', encoding='utf_8')

sentences = []
sentence = []
label_set = set()
cnt_line = 0
for line in f:
    cnt_line += 1
    if len(line) == 0 or line[0] == '\n':
        if len(sentence) > 0:
            sentences.append(sentence)
            print(sentence)
            sentence = []
        continue
    splits = line.split(' ')
    sentence.append([splits[0], splits[-1][:-1]])
    label_set.add(splits[-1])

if len(sentence) > 0:
    sentences.append(sentence)
    sentence = []
f.close()

for sen in sentences:
    i = 0
    for index, word in enumerate(sen):
        char = word[0]
        label = word[1]
        if index < len(sen) - 1:
            if (label[0] == 'B'):
                if sen[index + 1][1][0] == 'I':
                    label = label
            elif (label[0] == 'I'):
                if sen[index + 1][1][0] == 'I':
                    label = label
                if sen[index + 1][1][0] == 'O' or sen[index + 1][1][0] == 'B':
                    label = 'E' + label[1:]
            elif (label[0] == 'O'):
                label = label
        else:
            if (label[0] == 'B'):
                label = label
            elif (label[0] == 'I'):
                label = label
            elif (label[0] == 'O'):
                label = label

        f1.write(char+" "+label+'\n')
    f1.write('\n')
f1.close()
