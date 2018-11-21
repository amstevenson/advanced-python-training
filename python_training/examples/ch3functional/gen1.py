def evens():
    value = 0
    while True:
        yield value
        value += 2


gen_evens = evens()
print(next(gen_evens))
print(next(gen_evens))
print(next(gen_evens))
print(next(gen_evens))
