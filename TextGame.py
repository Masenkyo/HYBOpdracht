def vraag1():
    print(''' 
    Je word wakker en zet de tv aan, je ziet dat er een misschien een oorlog aankomt.
    A.	Je vlucht naar een andere stad/land. B.	Je wacht het af.
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraagA2()
    elif inputText == "B" or inputText == "b":
        vraagB1()

def vraagA2():
    print(''' 
    Je bent onderweg en het word onrustig en je hoord harde knallen in de verte.
    A.	Je zoekt een andere route. B.   Je gokt het en gaat door.
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraagA3()
    elif inputText == "B" or inputText == "b":
        vraagA2b1()

def vraagA3():
    print(''' 
    Je hebt een veiligere route genomen, maar nu zijn er soldaten bij de grens.
    A.	Je vermijd ze. B.	Je vraagt of je er door mag.
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraagA4()
    elif inputText == "B" or inputText == "b":
        vraagA3b1()

def vraagA4():
    print(''' 
    Je bent eindelijk in een andere stad gekomen, maar je ziet dat het daar ook slecht eraan toe is.
    A.	Je probeerd in een ander land te komen met het gevaar dat je word gepakt. B.	Je wacht in de Bergen.
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraagA5()
    elif inputText == "B" or inputText == "b":
        vraagA4b1()

def vraagA5():
    print(''' 
    Je bent nu in een ander land, maar het land wilt je misschien niet asiel geven.
    A.	Je negeert het land en probeerd naar een ander land door te lopen. B.	Je vraagt asiel.
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraagA6()
    elif inputText == "B" or inputText == "b":
        vraagA5b1()

def vraagA6():
    print(''' 
    Je komt mensen tegen die ook hetzelfde idee hadden.
    A.	Je reist met ze mee. B.	Je vertrouwt ze niet en reist alleen.
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraagA7()
    elif inputText == "B" or inputText == "b":
        vraagA6b1()

def vraagA7():
    print(''' 
    Het groepje verraad je en je ben vermoord… (ze waren undercover om mensen te vinden die waren gevlucht)
    ''')

def vraagB1():
    print(''' 
    Je stad is ingesloten en word bestormt met soldaten.
    A.	Je verstopt je in je huis. B.	Je probeert tegen te vechten.
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraagB1a1()
    elif inputText == "B" or inputText == "b":
        vraagB2()

def vraagB1a1():
    print(''' 
    Je overleeft voor 20 dagen en ze vinden je.
    A.	Terug vechten. B.	Je laat ze je oppakken.
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraagB1a2()
    elif inputText == "B" or inputText == "b":
        vraagB1a1b1()

def vraagB1a1b1():
    print(''' 
    Je liep naar ze toe maar je stapte in een val en je viel dood…
    ''')


def vraagB1a2():
    print(''' 
    Ze schieten je dood, omdat ze ingevaar waren…
    ''')

def vraagB2():
    print(''' 
    Je hebt een paar soldaten gedood en mensen die ook meevechten hebben je gered omdat je was gestoken met een mes en er werd een kogel in je hand geschoten…
    A.	Je laat je team een doctor zoeken. B.	Je zegt dat ze je moeten achterlaten.
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraagB2a1()
    elif inputText == "B" or inputText == "b":
        vraagB3()

def vraagB3():
    print(''' 
    Je bloed erg en je zoekt eten in het bos.
    A.	Je eet insecten en planten. B.	Je eet niks omdat je het te vies vind.
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraagB3a1()
    elif inputText == "B" or inputText == "b":
        vraagB4()

def vraagB4():
    print(''' 
    Je bent verhongerd en dood gebloed…
    ''')

def vraagB2a1():
    print(''' 
    De docter was slecht en heeft je laten leeg bloeden…
    ''')

def vraagB3a1():
    print(''' 
    Je overleeft en je wonden genezen langzaam aan.
    A.	Trek de kogel uit je hand. B.	Wacht met de kogel uit je hand trekken.
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraagB3a2()
    elif inputText == "B" or inputText == "b":
        vraagB3a1b1()

def vraagB3a2():
    print(''' 
    Je bloedde dood...
    ''')

def vraagB3a1b1():
    print(''' 
    Je steek wond is genezen aangezien hij niet heel diep was en je schotwond is bijna genezen.
    A.	Je houd hem in je hand. B.	Je haalt hem eruit voordat er enige infecties komen.
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraagB3a1b1a1()
    elif inputText == "B" or inputText == "b":
        vraagB3a1b2()

def vraagB3a1b1a1():
    print(''' 
    Je krijgt een infectie door de kogel en je gaat dood…
    ''')

def vraagB3a1b2():
    print(''' 
    Je trekt hem eruit en er komt bloed uit maar omdat je genoeg heb gegeten heb je weer bloed erbij gekregen dus je gaat er niet dood aan. Je hoord mensen schreeuwen in de verte.
    A.	Ernaartoe gaan en kijken wat er gebeurt. B.	Je probeerd uit je land te komen.
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraagB3a1b2a1()
    elif inputText == "B" or inputText == "b":
        vraagB3a1b3()

def vraagB3a1b3():
    print(''' 
    Je weet niet waar je bent en je durft niet met mensen te praten, dus je ging dood omdat er geen eten voor je was…
    ''')

def vraagB3a1b2a1():
    print(''' 
    Je ziet het leger dat je stad had bestord en ze verliezen tegen iedereen die meevecht.
    A.	Je loopt naar ze toe. B.	Je rent weg naar een ander land aangezien je nu weet waar je bent.
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraagB3a1b2a2()
    elif inputText == "B" or inputText == "b":
        vraagB3a1b2a1b1()

def vraagB3a1b2a2():
    print(''' 
    Het blijkt dat de mensen die meevochten al dood waren end at het leger enige mensen nog probeerde te lokken en ze namen je gevangen. Je zit nu in een gevangenis.
    A.	Je pleegt zelfmoord. B.	Je wacht totdat je word gesafed binnen 30 dagen anders word je gedood.
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraagB3a1b2a3()
    elif inputText == "B" or inputText == "b":
        vraagB3a1b2a2b1()

def vraagB3a1b2a2b1():
    print(''' 
    Je redde het niet...
    ''')

def vraagB3a1b2a3():
    print(''' 
    Je hebt jezelf vermoord…
    ''')

def vraagB3a1b2a3b1():
    print(''' 
    Je werd niet gered en je werd vermoord…
    ''')

def vraagB3a1b2a1b1 ():
    print(''' 
    Je komt aan in turkije en je vraagt om asiel. Een tijdje later word je afgewezen, maar je mag wel met een vliegtuig naar nederland.
    A.	Je vliegt naar nederland. B.	Je gaat terug naar je land en gaat dood (Kies dus niet deze xD)
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraagB3a1b2a1b1a1()
    elif inputText == "B" or inputText == "b":
        vraagB3a1b2a2b2()

def vraagB3a1b2a2b2 ():
    print(''' 
    Je gaat dood…
    ''')

def vraagB3a1b2a1b1a1():
    print(''' 
    Je komt aan in nederland.
    A.	Vraag om asiel. B.	Probeer illegal in nederland te leven.
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraagB3a1b2a1b1a2()
    elif inputText == "B" or inputText == "b":
        vraagB3a1b2a1b1a1b1()

def vraagB3a1b2a1b1a2():
    print(''' 
    B3a1b2a1b1a2 Je wacht 1 jaar en je krijgt asiel! (Good ending)
    ''')

def vraagB3a1b2a1b1a1b1():
    print(''' 
    Je word gepakt en je word terug gestuurd naar je land… (Je vliegtuig werd neergeschoten in je land…
    ''')

def vraagA2b1():
    print(''' 
    Je werd geraakt in crossfire en je bloede dood…
    ''')

def vraagA3b1():
    print(''' 
    Je word gepakt en word in een gevangenis gegooit.
    A.	Kill je zelf. B.	Wacht tot je word gedood (na 30 dagen).
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraagA3b1a1()
    elif inputText == "B" or inputText == "b":
        vraagA3b2()

def vraagA3b1a1():
    print(''' 
    Je hebt jezelf vermoord…
    ''')

def vraagA3b2():
    print(''' 
    Er ging een bom af in de gevangenis en je werd erdoor geraakt.
    A.	Probeer een docter te zoeken. B.	Je blijft liggen op de grond.  
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraagA3b2a1()
    elif inputText == "B" or inputText == "b":
        vraagA3b3()

def vraagA3b3():
    print(''' 
    Je bloed dood…
    ''')

def vraagA3b2a1():
    print(''' 
    Er is geen docter en je kan niet zwemmen, je bloed dood… 
    ''')

def vraagA4b1():
    print(''' 
    Je werd gevonden en ze dachten dat je ze ambushde dus ze schoten je dood…
    ''')

def vraagA5b1():
    print(''' 
    Je krijgt geen asiel en ze willen je geen vliegticket geven om naar een ander land te vluchten… je word terug gestuurd.
    A.	Je probeert in een vliegtuig te stappen illegal. B.	Je gaat naar je land.
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraagA5b1a1()
    elif inputText == "B" or inputText == "b":
        vraagA5b2()

def vraagA5b2():
    print(''' 
    Je stapte op een landmijn...
    ''')

def vraagA5b1a1():
    print(''' 
    Het lukt je op 1 of andere manier en je komt aan in nederland.
    A.	Vraag asiel. B.	Je gaat illegaal leven in nederland.
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraagA5b1a2()
    elif inputText == "B" or inputText == "b":
        vraagA5b1a1b1()

def vraagA5b1a1b1():
    print(''' 
    je bent gepakt en je word na 5 jaar gevangenis vrij gelaten en krijgt asiel.
    ''')

def vraagA5b1a2():
    print(''' 
    Je wacht anderhalf jaar en je krijgt asiel! (Good ending)
    ''')

def A5b1a1b1():
    print(''' 
    Je word niet gepakt maar het leven is moeilijk. (Neutral ending)
    ''')

def vraagA6b1():
    print(''' 
    Je komt aan in turkije en komt iemand tegen die zegt dat hij je met een private jet naar nederland kan brengen.
    A.	Je zegt ja en jullie beginnen met vliegen. B.	Je negeert hem en probeert weg te lopen.
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraagA6b1a1()
    elif inputText == "B" or inputText == "b":
        vraagA6b2()

def vraagA6b2():
    print(''' 
    Je probeerde weg te komen maar je werd neergestoken…
    ''')

def vraagA6b1a1():
    print(''' 
    De vliegtuig werd vol gezet met slaapgas en je word wakker in een martelkamer.
    A.	Je pleegt zelfmoord. B.	Je probeerd er doorheen te leven en misschien te ontsnappen.
    ''')
    inputText = input()
    print(inputText)
    if inputText == "A" or inputText == "a":
     vraagA6b1a2()
    elif inputText == "B" or inputText == "b":
        vraagA6b1a1b1()

def vraagA6b1a1b1():
    print(''' 
    Je ging dood…
    ''')

def vraagA6b1a2():
    print(''' 
    Je ging dood…
    ''')

def vraagA6b2():
    print(''' 
    Ze zagen dat je probeerde jezelf los te maken van het touw en ze schoten je dood…
    ''')

vraag1()