# find the pythagorean triplet for which abc = 1000

def gen_pythagorean_triples(search_for, start):
    for m in range(1, start):
        for n in range(1, m):
            a = (m * m) - (n * n)
            b = 2 * m * n
            c = (n * n) + (m * m)

            print("m = {0}, n = {1}".format(m, n))
            print("a = {0}, b = {1}, c = {2}".format(a, b, c))
            print("abc = {0}".format(a + b + c))
            if a+b+c == search_for:
                print(a * b * c)
                exit(0)
    gen_pythagorean_triples(search_for, start + 1)

gen_pythagorean_triples(1000, 5)