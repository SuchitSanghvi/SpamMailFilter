from mailparser import MailParser
import Tokenizer
import xlsxwriter


file = open("SPAMTrain.label",'r')

strt = file.read()
length = len(strt)

i = 0

label = []

label.append(strt[0])

for char in strt:
    if(ord(char)==10):
        if(i<length-1):
            label.append(strt[i+1])

    if(len(label)==41):
        break

    i = i + 1
    print(i)

print(label)

parser = MailParser()

spam = ""
ham = ""

no_of_spam=0
no_of_ham=0

i = 0

for lab in label:
    a = str(i)
    if(i<10):
        a = "00"+a
    elif(i < 100):
        a = "0" +a
    else:
        a = a;
    f = "TRAINING/TRAIN_00" +a+ ".eml"
    print(f)
    parser.parse_from_file(f)
    print(lab)
    if(lab=='0'):
        spam += parser.body
        no_of_spam += 1
    elif(lab=='1'):
        ham += parser.body
        no_of_ham += 1

    i=i+1


ferqofspam = Tokenizer.freqdata(spam)
print(ferqofspam)

print(no_of_spam)
ferqofham = Tokenizer.freqdata(ham)
print(ferqofham)

print(no_of_ham)


PR_S = no_of_ham/(no_of_ham+no_of_spam)
PR_H = no_of_spam/(no_of_ham+no_of_spam)

print(PR_S)
print(PR_H)

workbook = xlsxwriter.Workbook('spam.xlsx')
worksheet = workbook.add_worksheet()

i=1

for keys in ferqofspam.keys():
    # print(keys+str(ferqofspam.get(keys)))
    p = (int((ferqofspam.get(keys)/20)*no_of_spam))/no_of_spam
    # p = ferqofspam.get(keys) / no_of_spam
    worksheet.write('A'+str(i), keys)
    worksheet.write('B'+str(i), str(p))
    i+=1

workbook.close()
print("spam xslx done")

i=1

workbook = xlsxwriter.Workbook('ham.xlsx')
worksheet = workbook.add_worksheet()

for keys in ferqofham.keys():
    # print(keys+str(ferqofham.get(keys)))
    p = (int((ferqofham.get(keys)/10)*no_of_ham))/no_of_ham
    # p = ferqofham.get(keys) / no_of_ham
    worksheet.write('A'+str(i), keys)
    worksheet.write('B'+str(i), str(p))
    i+=1

workbook.close()
print("ham xsls done")
