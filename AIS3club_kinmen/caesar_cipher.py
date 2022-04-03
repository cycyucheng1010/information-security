def caesar(text,n):
    result = str()
    for i in range(len(text)):
        a  = text[i]
        if ord(a) != 32:
            if ord(a) < 97:
                result += chr((ord(a) + n-65) % 26 + 65)
            else:
                result += chr((ord(a) + n - 97) % 26 + 97)
        else:
            result += " "
    return result

msg = input()
n = int(input())
print (caesar(msg,n))