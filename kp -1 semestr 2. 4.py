a = list(complex(i) for i in input().split())
print({i.real: i.imag for i in a})
