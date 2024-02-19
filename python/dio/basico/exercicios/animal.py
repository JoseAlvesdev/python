animais = {
    'vertebrado': {'ave': {'carnivoro': 'aguia', 'onivoro': 'pomba'},
                   'mamifero': {'onivoro': 'homem', 'herbivoro': 'vaca'} 
                    },
    'invertebrado': {'inseto': {'hematofago': 'pulga', 'herbivoro': 'lagarta'},
                     'anelideo': {'hematofago': 'sanguessuga', 'onivoro': 'minhoca'}
                    }
}

#a, b, c = input().split()
a, b, c = input(), input(), input()

print(animais[a][b][c])