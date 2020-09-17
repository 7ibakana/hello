def convert(s):
    if (len(s) == 0):
        return
    s1 = ''
    s1 += s[0].lower()
    for i in range(1, len(s)):
        if (s[i] == ' '):
            s1 += s[i + 1].upper()
            i += 1
        elif (s[i - 1] != ' '):
            s1 += s[i].lower()
    print(s1)


# Driver Code
def main():
    s = input("Enter a fun sentence ")
    convert(s)


if __name__ == "__main__":
    main()