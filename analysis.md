
## Zdania wejściowe

Użytkownik może przekazać, czego oczekuje od programu poprzez:
-   zdania rozkazujące,
-   prośby,
-   sugestie.

#### Zdania rozkazujące:

-   do it -- 'VB' + 'PRP'
-   run it -- 'VB' + 'PRP'

#### Prośby:

-   would you do it -- [('would', 'MD'), ('you', 'PRP'), ('do', 'VB'), ('it', 'PRP')]
-   can you do it -- 'MD' + 'PRP' + 'VB' + 'PRP'
-   will you do it -- 'MD' + 'PRP' + 'VB' + 'PRP'
-   could you do it -- 'MD' + 'PRP' + 'VB' + 'PRP'
-   I would like you to do it -- [('I', 'PRP'), ('would', 'MD'), ('like', 'VB'), ('you', 'PRP'), ('to', 'TO'), ('do', 'VB'), ('it', 'PRP')]

#### Sugestie:

-   why don't you do it
-   how about you do it

## Rozpoznanie czasownika:

W większości wymienionych przykładów pierwszy element otagowany 'VB' jest czasownikiem, który wyraża, co chcemy, aby nasz program wykonał.

Wyjątkiem są zdania typu: "I'd like you to do it", gdzie pierwszym 'VB' jest czasownik modalny 'like'. Z tego powodu upewniam się, że przed rozpatrywanym przeze mnie 'VB' nie znajduje się czasownik 'MD'. Przy innych przykładach (sugestie) nie będzie stanowić to problemu, gdyż tam musimy po czasowniku modalnych podać 'you' ('PRP').

## Rozpoznanie obiektu:

W każdym z powyżej wymienionych przykładów obiekt, na którym chcemy wykonać akcję, znajduje się zaraz po czasowniku. W przypadku wyszukiwania jako frazę traktuję wszystko co występuje po czasowniku 'search'/'google'.

## Wpływ obiektu na czasownik:

W zdaniu "open it" otrzymamy otagowanie [('open', 'VB'), ('it', 'PRP')], natomiast w zdaniu "open yay.jpg" dowiemy się, ze 'open' zostało otagowane jako przymiotnik:

[('open', 'JJ'), ('yay.jpg', 'NN')]

Z tego powodu wprowadziłam listę wyjątków dla czasowników, które w analogicznych sytuacjach również są otagowane niepoprawnie.

## Czasowniki inne niż zadane:

Aby nie ograniczać użytkownika do jednego rodzaju polecenia, wprowadziłam również możliwość korzystania z synonimów.

Np. wprowadzenie "launch it" wykona taką samą akcję jak "run it".

W tym celu chciałam skorzystać z wordnet i wyszukiwania synonimów, jednak napotkałam problem przy słowach typu 'open', ponieważ funkcja analizowała to słowo jako przymiotnik. Niestety nawet w przypadkach, kiedy szukałam faktycznych synonimów do czasowników, ich lista bywała okrojona i bardzo podstawowa.

Z tych powodów sama określiłam dla każdego czasownika ich synonimy w słowniku.
