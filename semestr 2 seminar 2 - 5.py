def ne_france(a,b,c):
    a = set(a)
    b = set(b)
    c = set(c)
    d = (b & c) - a
    return d

learners_french = ['Sasha','Dasha','Yasha','Kasha']
pianists = ['Pasha','Masha','Yasha']
swimmers = ['Pasha','Masha','Sasha','Dasha','Yasha']
print(list(ne_france(learners_french,pianists,swimmers)))