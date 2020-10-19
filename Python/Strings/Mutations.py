def mutate_string(string, position, character):
    word = list(string)
    word[position] = character
    return "".join(word)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)