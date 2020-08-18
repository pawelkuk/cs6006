import numpy as np

LINE = 80


def fit(line):

    length_line = sum(line) + len(line) - 1

    return (LINE - length_line) ** 3 if length_line < LINE else float("inf")


def reconstruct_text(words, breaks):

    lines = []
    linebreaks = []

    i = 0
    while True:

        linebreaks.append(breaks[i])
        i = breaks[i]

        if i == len(words):
            linebreaks.append(0)
            break

    for i in range(len(linebreaks)):
        lines.append(" ".join(words[linebreaks[i - 1] : linebreaks[i]]).strip())  # noqa

    return lines


with open("./data/lorem.txt", "r") as file:
    text = file.read()
    words = text.strip().replace("\n", "").split(" ")
lens = [len(word) for word in words]

memo = [0] * (len(lens) + 1)
s = [0] * (len(lens) + 1)
for i in range(len(lens) - 1, -1, -1):
    tmp = []
    for k in range(i + 1, len(lens) + 1):
        f = fit(lens[i:k])
        if f == float("inf"):
            break
        else:
            tmp.append(memo[k] + f)
    print(i, tmp)
    index = np.argmin(tmp)
    s[i] = index + i + 1
    memo[i] = tmp[index]
print(memo)
print(s)


print("\n".join(reconstruct_text(words, s)))
