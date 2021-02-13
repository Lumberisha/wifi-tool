# Siguria ne internet - detyra 3

## Kerkesa e detyres

Zhvillimi i aplikacionit qe mundeson leximin e te gjithe passwordeve te ruajtur te wifi-ve dhe vizuelizon
kompleksitetin ne forme grafi duke marre parasysh disa kritere.

</br>

## Pershkrimi i aplikacionit

Aplikacioni qellim kryesor ka nxjerrjen e fjalekalimev te ruajtura ne PC. Ne sistemin operativ windows perdoret komanda `netsh wlan show profile <name> key=clear`. Kompleksiteti i fjalekalimit eshte bere duke u bazuar ne disa parime:

- Fjalekalim i veshtire > permban te pakten nje shkronje te vogel, nje shkronje te madhe, nje numer dhe nje simbol.

- Fjalekalim mesatarisht i veshtire > permban 3 nga kombinimet e lartecekura.

- Fjalekalim i lehte > permban 2 nga kombinimet e lartecekura.

- Fjalekalim shume i lehte > permban vetem shkronja ose numra.

</br>

## Instalimi i aplikacionit

### Librarite e perdorura

- subprocess
- re
- numpy
- matplotlib > duhet te instalohet permes komandes `pip install matplotlib`

Per vizualizim te kompleksitetit te te dhenave eshte perdorur libraria matplotlib.

Ekzekutimi i aplikacionit behet duke perdorur komanden `python main.py`

### Shembulli i ekzekutimit

<br>
<br>
<br>
<br>


![Untitled](https://user-images.githubusercontent.com/44115091/107861566-f5784c80-6e46-11eb-9830-71e9d61d428e.png)
