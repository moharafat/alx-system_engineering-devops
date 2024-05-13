def unique(str):
    for letter in str:
        index +=1
        for i in range(index, len(str)):
            if letter == str[i]:
                return False
    return True

if __name__ == "__main__":
    print(unique("install"))
    print(unique("instal"))
