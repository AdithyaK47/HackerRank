def split_and_join(line):
    wordList = line.split(" ")
    return "-".join(wordList)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)