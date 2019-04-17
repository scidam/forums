import re
import random

consonants_pat = 'BCDFGHJKLMNPQRSTVXZ'.lower()
vowels_pat = 'aeiouy'

train_data = '''
                This our sentence to be used as a training dataset
                It should be longer
                '''

def build_mixer(train_data, num=3, mixed_len=(2, 4)):
    
    def _get_random_pattern(td, wlen):
        td_splitted = td.lower().split()
        while True:
            w = random.choice(list(filter(lambda x: len(x)>=wlen, td_splitted)))
            for j in range(len(w)-wlen):
                yield tuple(map(lambda x: 0 if x in vowels_pat else 1,  w[j:j + wlen]))

    def _select_vowels(w):
        return 
    
    
    def _mixer(w1, w2, num=num, mixed_len=mixed_len):
        allowed_letters = w1.lower().strip() + w2.lower().strip()
        ind = 1
        for j in range(num):
            wlen = random.choice(range(*mixed_len))
            pattern = _get_random_pattern(train_data, wlen)
            _aux = allowed_letters
            word = ''
            try:
                for pat in pattern:
                    for k in pat:
                        if k == 0:
                            choiced = random.choice(list(filter(lambda x: x in vowels_pat,  _aux)))
                            word += choiced
                        else:
                            choiced = random.choice(list(filter(lambda x: x in consonants_pat,  _aux)))
                            word += choiced
                        l = list(_aux)
                        l.remove(choiced)
                        _aux = ''.join(l)
                    ind += 1
                    yield word
                    if ind>num:
                        raise StopIteration
            except IndexError:
                continue

    return _mixer


mixer = build_mixer(train_data, num=6, mixed_len=(3,6))
for mixed in mixer('this', 'horse'):
    print(mixed)
