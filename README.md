## solidabisHaaste2019

koodihaaste.solidabis.com

### Tehtävänanto
Tehtävänäsi on purkaa APIsta haettuja kryptattuja lauseita. Lauseet on kryptattu Caesar-salakirjoitusjärjestelmällä kirjaimia oikealle siirtämällä. Aakkostona toimii A-Ö. Kirjainkoolla ei ole merkitystä. Jokaisen lauseen avain on satunnainen. Käännettävissä olevat lauseet ovat suomea. Mukana on myös lauseita, jotka eivät käänny selkokieliseksi millään avaimella.

Sinun tulee luoda web-käyttöliittymä, joka näyttää lauseet jaoteltuina No bullshit ja bullshit –lauseisiin. Käännettävissä olevat no bullshit –lauseet näytetään suomeksi ja bullshit-lauseet, jotka eivät käänny selkokielisiksi, näytetään alkuperäismuodossaan.

Et saa käyttää mitään kolmannen osapuolen palvelua tai kirjastoa, joka tunnistaa kielen automaattisesti. Tekstiaineistojen, kuten sanakirjan käyttö on kuitenkin sallittua, joskin annamme lisäpisteitä ratkaisuista, jotka eivät tukeudu valmiisiin aineistoihin.

Toteutukseen käytettävät teknologiat ovat vapaasti päätettävissäsi.


### Totetus
Python + Flask kikkana joka noutaa viestit solidabiksen apilta -> käsittely ja siitä sitten frontille pusku.

@ToDo: Kielen tunnistaminen hyvällä varmuudella - Gibberish vs Suomi
@ToDo: Frontin rakennus
