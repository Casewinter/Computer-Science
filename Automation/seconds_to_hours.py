import math

def s(n):
    n = str(n)[-2::]
    m = n[0]
    if int(m) > 6:
        return f"5{n[1]}"
    return n


def make_readable(seconds):
    hours = math.floor(seconds / 3600)
    minutes = math.floor(seconds / 60 % 60)
    seconds = seconds % 60
    f = list([hours, minutes, seconds])
    for i, n in enumerate(f):
        f[i] = str(n).zfill(2)

    return ":".join(f)


print(make_readable(3599))




