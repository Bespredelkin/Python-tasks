letter = str(input())
st = str(input())

try:
    a = st.index(letter)
    b = st.rindex(letter)
except (ValueError ):

    print(None, None)
else:
    print(a, b)