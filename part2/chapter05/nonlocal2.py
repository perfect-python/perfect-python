def outer():
    var1 = '外側の変数'
    var2 = 'これも外側の変数'

    def inner():
        nonlocal var1

        var1 = '内側で変更'
        var3 = '内側の変数'
        return (var1, var2, var3)

    return inner()
