import torch
import matplotlib.pyplot as plt

names = open("names.txt", "r").read().splitlines()

bigram_dict = {}

N = torch.zeros((28, 28), dtype=torch.int32)

chars = sorted(list(set(''.join(names))))
stoi = {s:i for i, s in enumerate(chars)}

stoi["<S>"] = 26
stoi["<E>"] = 27

for name in names:
    letters = ["<S>"] + list(name) + ["<E>"]
    for ch1, ch2 in zip(letters, letters[1:]):
        bigram = (ch1, ch2)
        bigram_dict[bigram] = bigram_dict.get(bigram, 0) + 1
        ix1 = stoi[ch1]
        ix2 = stoi[ch2]
        N[ix1, ix2] += 1

itos = {i:s for s, i in stoi.items()}

plt.figure(figsize=(10,10))
plt.imshow(N, cmap="Blues")

#Graph plot for alphabet bigrams
#for i in range(28):
#    for j in range(28):
#        chstr = itos[i] + itos[j]
#        plt.text(j, i, chstr, ha="center", va="bottom", color="gray")
#        plt.text(j, i, N[i, j].item(), ha="center", va="top", color="gray")
#plt.axis("off")
