var1 = 'グローバル'


def spam():
    global var1

    var1 = 'ローカルで変更'
    var2 = 'ローカル'
    return (var1, var2)
