from uzwords import words
from difflib import get_close_matches

def checkWords(word:str,words=words):
    word=word.lower()
    matches=set(get_close_matches(word,words))
    available=False
    if word in matches:
        available=True
        matches=word
    elif 'ҳ' in word:
        word=word.replace('ҳ','х')
        matches.update(get_close_matches(word,words))
    elif 'х' in word:
        word = word.replace('х','ҳ')
        matches.update(get_close_matches(word, words))
    return {'available':available,'matches':matches}
if __name__=='__main__':
    print(checkWOrds("тариҳ"))


