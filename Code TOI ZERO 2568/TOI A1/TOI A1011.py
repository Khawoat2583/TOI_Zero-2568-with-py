a = str(input())
def etm(message):
    if len(message) != 5 or not message.isalpha() or not message.isupper():
        return
    result = ""
    count = 1
    for i in range(1, len(message)):
        if message[i] == message[i - 1]:
            count += 1
        else:
            result += str(count) + message[i - 1]
            count = 1
    result += str(count) + message[-1]
    return result
print(etm(a))
