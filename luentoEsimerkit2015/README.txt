Virtauslaskenta 2015
TTY
Antti Mikkonen

OpenSource luennolla käsitellyt tapaukset ja hieman selitystä.
Ideana että koska kukaan ei voi oppia komentorivikäskyjä ulkoa 
yhdellä näkemällä niin tässä on valmiit tiedostot joista kopioda.

Huomaathan että mikään näistä esimerkeistä ei ole laskettu "oikein". Kaikki
tapaukset ovat tarkoituksella tehty laskennallisesti kevyiksi luotettavuuden
kustannnuksella.

cad 
Salome tiedosto Study1.hdf. 
dump.py on salome tiedostoa vastaava Python dump.
stl tiedostot sisältävät pinnat valmiina.

helyxVersion
Helyxin generoima tiedosto rakenne juuri sellaisena kuin se Helyxistä tulee ulos.
Vain aika-askeleihin liittyvä tieto poistettu kokoa pienentääkseen. Aukeaa 
Helyxilla suoraan ja pitäisi lähteä laskemaan kun painaa "Run"-nappia.

cliVersion
Helyx laskennasta siivottu komentorivi versio. Lähtee käyntiin kun ajaa 
komentorivillä käskyn
    bash solver.sh
Hieman siistimpi kuin luennolla tehty esimerkki mutta vastaava.
Tiedostossa muunnos on lisäksi komentoja joilla saa Helyxin tuottamasta
rinnakkaiseen ajoon tarkoitetusta rakenteesta muokattua sarjallisen.
Tiedostossa plotResidual.sh on residuaalien plottaukseen käytetty komento. 

cliSerialVersion
Luennolla laskenta tehtiin rinnakkaisena. Tämä on kuitenkin tarpeetonta ellei
tehtävä laskenta ole raskas. Itse asiassa olisi ollut järkevämpää jättää
rinnakkaistaminen tekemättä seuraamisen helpottamiseksi. Tässä sarjallinen 
ratkaisu. Muuten sama kuin cliVersion. Käytännössä pari komentoa puuttuu 
välistä.

autoVersion
Automatisoitu cliVersion. Tiedostossa solver.sh rivillä 10 on loitsu joka 
muuttaa tiedostossa 0/U olevaa pienen putken tilavuusvirtaa. Tiedosto 0/U
luodaan ajon aikana. Tiedostossa 0.org/U on muutoksia riviveillä 18 ja 65. 
Nämä muutokset helpottavat parametrisointia. Ajo tapahtuu lisäämällä parametri
cliVersion ajokomennon perään. Esim tilavuus virralle 0.0001963495
    bash solver.sh 0.0001963495
Muuten vastaava kuin cliVersion.

sarja.sh
Bash scripti joka ajaa sarjan laskentoja. Luo tiedostot auto1, auto2, auto3, 
auto4 ja auto5. Ajaa laskennat. Kirjoittaa pienenputken paineen tiedostoon 
tulos sitä mukaa kun lasketa valmistuu. Lähtee käyntiin komennolla
    bash sarja.sh 

virtauslaskenta2015_opensource.pdf
Sama tiedosto joka oli POPissa jaossa ennen luentoa. Ohjeet virtuaalikoneen
käyttöön ja speksi ohjelmistosta.

cfMeshSerialVersion
Extrana vielä omalla suosikki verkottajallani tehty sarjallinen laskenta. 
Erona lähinnä ylimääräisen siivoaminen, esim. geometrian luonti pois ja 
uusi tiedosto system/meshDict joka määrittää verkon. Lisäksi symmetria jätetty 
pois, tilavuusvirtoja ei korjattu. Lisäksi cfMesh haluaa että kaikki 
stl-komponentit ovat samassa tiedostossa. Tämän tiedoston nimi on 
constant/triSurface/putki.stl. Ajetaan käskyllä 
    bash solver.sh

Lisäksi kannattaa perehtyä OpenFOAMin mukana tuleviin tutoriaaleihin, jotka 
löytyvät komennolla
    cd $FOAM_TUTORIALS
Internet on myös pulloon tutoriaaleja ja lisää saa tulla kysymään. 

Happy Foaming,
Antti Mikkonen
K1307

    


