from ib111 import week_07  # noqa

# Jistě už jste někdy slyšeli o hře Tetris. Pokud ne, vítejte v civilizaci!
# Hledat můžete začít například tady: ‹https://duckduckgo.com/?q=tetris›.
# V tomto domácím úkolu si klon této hry naprogramujete.
#
# Abyste si hru mohli vyzkoušet (poté, co implementujete všechny níže
# uvedené metody), je vám k dispozici soubor ‹game_tetris.py›, který vložte do
# stejného adresáře, jako je soubor s vaším řešením, případně jej upravte
# dle komentářů na jeho začátku a spusťte.
# Hra se ovládá těmito klávesami:
#
# • pohyb doleva: šipka doleva nebo ‹A›,
# • pohyb doprava: šipka doprava nebo ‹D›,
# • pohyb dolů: šipka dolů nebo ‹S› (děje se také automaticky s nastavenou
#   prodlevou),
# • rychlý pád dolů: mezerník,
# • otočení proti směru hodinových ručiček: ‹Q› nebo Page Up,
# • otočení po směru hodinových ručiček: ‹E› nebo Page Down,
# • ukončení hry: ‹X›,
# • restart: ‹R›.
#
# Třída ‹Tetris›, kterou máte implementovat, reprezentuje stav hry, tj. obsah
# herní oblasti (již spadlé kostky), aktuálně padající blok, jeho pozici
# a aktuální skóre. Způsob reprezentace je na vás. Testy i grafické rozhraní
# používají ke komunikaci s vaší třídou pouze zde popsané metody.
#
# Rozměry herní oblasti budou zadány při inicializaci (funkci ‹__init__›).
# Všechny pozice mimo zadané rozměry považujeme za neprostupnou zeď.
# Souřadnice zde používáme ve tvaru (sloupec, řádek), přičemž pozice (0, 0)
# je v levém horním rohu herní oblasti. Čísla sloupců rostou zleva doprava,
# čísla řádků shora dolů.
#
# Padající bloky reprezentujeme seznamem relativních souřadnic, přičemž (0, 0)
# je střed otáčení. Tedy např. ‹[(-1, 0), (0, 0), (1, 0), (0, 1)]› je tetromino
# tvaru T otočené směrem dolů, které se bude otáčet kolem své prostřední
# kostky. Blok ‹[(-1, -1), (0, -1), (1, -1), (0, 0)]› má stejný tvar, ale otáčí
# se kolem své „spodní nožičky“. Střed otáčení nemusí být nutně součástí bloku,
# např. ‹[(-1, -1), (-1, 0), (-1, 1), (0, 1)]› je tetromino tvaru L, které se
# otáčí kolem prázdného místa ve svém rohu.
#
# Přestože se v grafickém rozhraní používají pouze tetromina (tedy klasické
# tetrisové bloky), vaše řešení musí být obecné a fungovat s libovolnými tvary
# bloků.
#
# «Poznámka:» Protože za zeď považujeme i prostor „nad“ herní oblastí, může se
# v mnoha případech stát, že blok, který se nově objevil, nebude možné otočit,
# dokud se neposune o něco níže. Ačkoli reálné implementace tuto možnost
# většinou nějak ošetřují, zde pro zjednodušení nic takového neděláme
# a považujeme to za očekávané chování.

Position = tuple[int, int]


class Tetris:

    # Po inicializaci by měla být herní oblast prázdná, o zadaných rozměrech.
    # Není žádný padající blok a skóre je nastaveno na 0.

    def __init__(self, cols: int, rows: int):
        self.cols = cols
        self.rows = rows
        self.current = None
        self.score = 0

    # Čistá metoda ‹get_score› vrátí aktuální skóre.

    def get_score(self) -> int:
        return self.score

    # Metoda-predikát ‹has_block› vrátí ‹True› právě tehdy, existuje-li
    # padající blok.

    def has_block(self) -> bool:
        return self.current is not None

    # Metoda ‹add_block› přidá do hry padající blok na zadaných souřadnicích.
    # Pokud přidání bloku není možné (překrýval by se s již položenými
    # kostkami), metoda situaci nezmění a vrátí ‹False›; jinak vrátí ‹True›.
    # Metoda bude volána pouze tehdy, neexistuje-li žádný padající blok.
    # Seznam ‹block› nijak nemodifikujte. Pokud si ho hodláte někam uložit,
    # tak buďto zaříďte, aby se ani později nemodifikoval, nebo si vytvořte
    # jeho kopii.

    def add_block(self, block: list[Position],
                  col: int, row: int) -> bool:
        for horizontal, vertical in block:
            x = row + horizontal
            y = col + vertical
            if x < 0 or x >= self.cols or y < 0 or y >= self.rows or self.tiles[x][y]:
                return False
        self.current = {"colision": block, "position": (col, row)}



    # Metoda ‹left› posune padající blok o jednu pozici doleva, je-li to možné.
    # Tato metoda, stejně jako všechny následující metody pohybu, bude volána
    # jen tehdy, existuje-li padající blok.

    def left(self) -> None:
        if self.current is None:
            return None
        form, (col, row) = self.current["colision"], self.current["position"]
        for x, y in form:
            move_col = col + x - 1
            move_row = row + y
            if move_col < 0 or self.tiles[move_col][move_row]:
                return None
            
        self.current["position"] = (col - 1, row)

        

    # Metoda ‹right› posune padající blok o jednu pozici doprava,
    # je-li to možné.

    def right(self) -> None:
        if self.current is None:
            return None
        form, (col, row) = self.current["colision"], self.current["position"]
        for x, y in form:
            move_col = col + x + 1
            move_row = row + y
            if move_col > self.cols or self.tiles[move_col][move_row]:
                return None
            
        self.current["position"] = (col + 1, row)
        

    # Metoda ‹rotate_cw› otočí padající blok po směru hodinových ručiček o 90
    # stupňů, je-li to možné.

    def rotate_cw(self) -> None:
        if self.current is None:
            return None
        form, (col, row) = self.current["colision"], self.current["position"]

        new_form = []
        for x, y in form:
            new_col = - y + col
            new_row = x + row
            if new_col < 0 or new_col >= self.cols or new_row < 0 or new_row >= self.rows or self.tiles[new_col][new_row]:
                return False
            new_form.append((new_col, new_row))
        
        self.current["colision"] = new_form
            
    # Metoda ‹rotate_ccw› otočí padající blok proti směru hodinových ručiček
    # o 90 stupňů, je-li to možné.

    def rotate_ccw(self) -> None:
        if self.current is None:
            return None
        form, (col, row) = self.current["colision"], self.current["position"]
        new_form = []

        for x, y in form:
            new_row = - x + row
            new_col = y + col
            if new_col < 0 or new_col >= self.cols or new_row < 0 or new_row >= self.rows or self.tiles[new_col][new_row]:
                return False
            new_form.append(new_col, new_row)
            
        self.current["colision"] = new_form
            


    # Metoda ‹down› posune padající blok o jednu pozici směrem dolů.
    # Pokud takový posun není možný, kostky z padajícího bloku se napevno
    # umístí do herní oblasti; zcela zaplněné řádky se pak z oblasti vymažou
    # a skóre se zvýší o druhou mocninu počtu vymazaných řádků.

    def down(self) -> None:
        if self.current is None:
            return None
        form, (col, row) = self.current["colision"], self.current["position"]
        for x, y in form:
            move_col = col + x
            move_row = row + y + 1

            if move_row > self.rows or self.tiles[move_col][move_row]:
                return None
            
        self.current["position"] = (col, row + 1)

    # Metoda ‹drop› shodí padající blok směrem dolů (o tolik pozic, o kolik je
    # to možné). Kostky z padajícího bloku se pak napevno umístí do herní
    # oblasti; zcela zaplněné řádky se pak z oblasti vymažou a skóre se zvýší
    # o druhou mocninu počtu vymazaných řádků.

    def drop(self) -> None:
        if self.current is None:
            return None
        form, (col, row) = self.current["colision"], self.current["position"]
        max_distance = self.rows
        for x, y in form:
            move_col = col + x
            move_row = row + y + 1
            distance = 0
            while y + distance < self.rows or self.tiles[move_col][move_row]:
                distance += 1
            max_distance = min(distance, max_distance)
            
            
        self.current["position"] = (col, row + max_distance)
        self.block_in_position()
        self.lane()
    

    def lane(self):
        pass
    
    
    def block_in_position(self):
        pass

    # Čistá metoda ‹tiles› vrátí seznam všech pozic, na nichž má být vykreslena
    # kostka – tedy jednak všechny položené kostky v herní oblasti, jednak
    # všechny kostky tvořící padající blok. Na pořadí pozic v seznamu nezáleží.
    # Tuto metodu používají jak testy pro ověření správnosti implementace,
    # tak grafické rozhraní pro vykreslení hry.

    def tiles(self) -> list[Position]:
        in_position = []

        if self.current:
            shape, (col, row) = self.current['colision'], self.current['position']
            for x, y in shape:
                in_position.append((col + x, row + y))
        
        return in_position


def main() -> None:
    tetris = Tetris(10, 22)

    assert tetris.get_score() == 0
    assert not tetris.has_block()
    assert tetris.tiles() == []

    block_s = [(1, -1), (0, -1), (0, 0), (-1, 0)]

    assert not tetris.add_block(block_s, 4, 0)
    assert not tetris.has_block()

    assert tetris.add_block(block_s, 4, 1)
    assert tetris.has_block()
    assert set(tetris.tiles()) == {(3, 1), (4, 0), (4, 1), (5, 0)}
    assert len(tetris.tiles()) == 4

    tetris.down()
    assert tetris.has_block()
    assert set(tetris.tiles()) == {(3, 2), (4, 1), (4, 2), (5, 1)}
    assert len(tetris.tiles()) == 4

    tetris.left()
    assert tetris.has_block()
    assert set(tetris.tiles()) == {(2, 2), (3, 1), (3, 2), (4, 1)}
    assert len(tetris.tiles()) == 4

    tetris.right()
    assert tetris.has_block()
    assert set(tetris.tiles()) == {(3, 2), (4, 1), (4, 2), (5, 1)}
    assert len(tetris.tiles()) == 4

    tetris.right()
    assert tetris.has_block()
    assert set(tetris.tiles()) == {(4, 2), (5, 1), (5, 2), (6, 1)}
    assert len(tetris.tiles()) == 4

    tetris.rotate_cw()
    assert tetris.has_block()
    assert set(tetris.tiles()) == {(5, 1), (5, 2), (6, 2), (6, 3)}
    assert len(tetris.tiles()) == 4

    tetris.rotate_ccw()
    assert tetris.has_block()
    assert set(tetris.tiles()) == {(4, 2), (5, 1), (5, 2), (6, 1)}
    assert len(tetris.tiles()) == 4

    tetris.rotate_ccw()
    assert tetris.has_block()
    assert set(tetris.tiles()) == {(4, 1), (4, 2), (5, 2), (5, 3)}
    assert len(tetris.tiles()) == 4

    tetris.drop()
    assert not tetris.has_block()
    assert set(tetris.tiles()) == {(4, 19), (4, 20), (5, 20), (5, 21)}
    assert len(tetris.tiles()) == 4

    assert tetris.get_score() == 0
    assert block_s == [(1, -1), (0, -1), (0, 0), (-1, 0)]


if __name__ == '__main__':
    main()
