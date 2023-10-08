def verificação_postagem_tuite():

    T = input()
    count = 0

    for caracter in T:
        if (type(caracter == str)):
            count += 1
        
    if (count <= 140):
        print('TWEET')
    else:
        print('MUTE')
        

verificação_postagem_tuite()