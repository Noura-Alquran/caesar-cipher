import re
import nltk

from nltk.corpus import words , names

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)
word_list = words.words()
name_list = names.words()


english_alphabets='abcdefghijklmnopqrstuvwxyz'

def encrypt(text,num):
    words=text.split()
    new_words=[]
    for word in words:
        new_word=''
        for i in word:
            if i.lower() != i and i.lower() in english_alphabets:
                number=(english_alphabets.index(i.lower())+num) %26
                new_word+=(english_alphabets[number].upper())
       
            elif i.lower() == i and i.lower() in english_alphabets:
                number=(english_alphabets.index(i)+num) %26
                new_word+=(english_alphabets[number])
            else :
                new_word+=i
        new_words.append(new_word) 
    return " ".join(new_words)


def decrypt(encrypted,key):
    return encrypt(encrypted,-key)


def count_words(text):
    candidate_words = text.split()
    word_count = 0
    for candidate in candidate_words:
        word = re.sub(r'[^A-Za-z]+','', candidate)
        if word.lower() in word_list or word in name_list:
            word_count += 1
        else:
            pass
    return word_count


def crack(encrypted):
    for i in range(0,26):
        text= decrypt(encrypted,i)
        percentage = int(count_words(text) / len(encrypted.split()) * 100)
        if percentage > 50:
            return text 
   


if __name__ == "__main__":
    print(encrypt('AbC nO jk1', 10))
    print(encrypt('ABC', 10))
    print(encrypt('abc', 10))
    print(encrypt('abc',1))
    print(encrypt('abc',27))
    print( encrypt('zzz', 1) )
    print( decrypt('aaa', 1) )
    print( decrypt('KlM xY tu1',10))
    print(count_words('I want to say something ghjklszs'))
    print(count_words('hjbjkdaLNK5 YES'))
    print(encrypt('I want to say something',5))
    print(crack('N bfsy yt xfd xtrjymnsl'))
    print(encrypt('I want to say something',25))
    print(crack('H vzms sn rzx rnldsghmf'))







