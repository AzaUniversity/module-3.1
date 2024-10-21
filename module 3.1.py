calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    stroka = str(string)
    result = (len(stroka), stroka.upper(), stroka.lower())
    count_calls()
    return result

def is_contains(string, list_to_search):  # 4
        string = str(string).lower()
        list_to_search = list(list_to_search)
        count_calls()
        for i in range(len(list_to_search)):
            if str(list_to_search[i]).lower() == string:
                result = True
                break
            else:
                result = False
                continue
        return result

print(string_info('Pikabu'))
print(string_info('Chizhik'))
print(is_contains('vouge', ['flik', 'jamp', 'esy']))
print(is_contains('BaNANA', ['neVERE', 'mOOn', 'veGETEble']))

print(calls)