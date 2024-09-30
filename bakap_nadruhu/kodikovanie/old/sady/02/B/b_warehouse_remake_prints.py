from ib111 import week_05  # noqa


# V tomto úkolu se budeme zabývat skladem zboží. Zboží je ve skladu uloženo po
# balících, které reprezentujeme trojicemi hodnot: množství (počet jednotek)
# zboží, jednotková cena zboží a datum exspirace. Všechny tři hodnoty budou
# vždy kladná celá čísla, přičemž datum exspirace bude vždy zadáno tak,
# aby jeho zápis v desítkové soustavě byl ve formátu ‹YYYYMMDD› dle ISO 8601.

Package = tuple[int, int, int]  # amount, price, expiration date


# Obsah skladu budeme reprezentovat seznamem balíků, přičemž tento seznam bude
# vždy seřazen sestupně dle data exspirace. (Je zájmem společnosti, které sklad
# patří, aby se jako první prodaly balíky, jejichž konec trvanlivosti se blíží;
# přitom balíky budeme prodávat od konce seznamu.)
#
# Nejprve implementujte funkci ‹remove_expired›, která ze skladu odstraní
# všechny balíky s prošlou trvanlivostí (tj. ty, jejichž datum exspirace
# předchází dnešnímu datu ‹today›, které je zadáno stejně jak je popsáno výše).
# Funkce vrátí seznam odstraněných balíků v opačném pořadí, než byly umístěny
# ve skladu.


def remove_expired(warehouse: list[Package],
                   today: int) -> list[Package]:
    removed = []
    reversed = []
    iter = 0
    for element in warehouse:
        _, _, date_ex = element
        if date_ex < today:
            removed.append(element)
            iter += 1
    for _ in range(iter):
        warehouse.pop()
    while removed != []:
        reversed.append(removed[-1])
        removed.pop()

    return reversed


# Dále pak implementujte funkci ‹try_sell›, která uskuteční prodej při zadaném
# maximálním množství ‹max_amount› a zadané maximální průměrné jednotkové ceně
# ‹max_price›. Přitom je cílem prodat co nejvíce zboží (v rámci respektování
# zadaných limitů). Prodávat je možno jak celé balíky, tak i jen jejich části;
# je tedy dovoleno existující balík rozbalit a odebrat z něj jen několik
# jednotek zboží (tím vlastně z jednoho balíku vzniknou dva – jeden zůstane ve
# skladu, druhý se dostane ke kupci). Je ovšem třeba postupovat tak, že se
# balíky odebírají pouze z konce seznamu reprezentujícího sklad – tj. není
# možno prodat balík (nebo jeho část), aniž by předtím byly prodány všechny
# balíky nacházející se v seznamu za ním. Funkce vrátí seznam balíků, které se
# dostaly ke kupci, a to v tom pořadí, jak se postupně ze skladu odebíraly.
#
# Pro příklad uvažujme sklad s následujícími balíky (datum exspirace zde
# neuvádíme, horní číslo je množství, spodní cena; pořadí balíků odpovídá
# seřazení seznamu, prodáváme tedy „zprava“):
#
#  ╭─────╮  ╭─────╮  ╭─────╮  ╭─────╮
#  │ 200 │  │  90 │  │ 100 │  │  42 │
#  ├─────┤  ├─────┤  ├─────┤  ├─────┤
#  │ 158 │  │  14 │  │  17 │  │  9  │
#  ╰─────╯  ╰─────╯  ╰─────╯  ╰─────╯
#     D        C        B        A
#
# • Pokud by přišel požadavek na prodej s maximálním množstvím 500 a maximální
#   průměrnou jednotkovou cenou 9, pak se prodá pouze celý balík ‹A›.
# • Pokud by místo toho byla požadovaná maximální průměrná cena 12, pak se
#   prodá celý balík ‹A› a 25 jednotek zboží z balíku ‹B›.
#   (Balík ‹B› se tedy rozdělí: ve skladu zůstane balík s množstvím 75, ke
#   kupci se dostane balík s množstvím 25.)
# • Pokud by byla požadovaná maximální průměrná cena 14, pak se prodá celý
#   balík ‹A› a 70 jednotek zboží z balíku ‹B›.
# • Pokud by byla požadovaná maximální průměrná cena 15, pak se prodají celé
#   balíky ‹A›, ‹B› a ‹C›.
# • Pokud by byla požadovaná maximální průměrná cena 16, pak se prodají celé
#   balíky ‹A›, ‹B›, ‹C› a dvě jednotky zboží z balíku ‹D›.
# • Konečně pro maximální průměrnou cenu 81 se prodají všechny balíky.


def try_sell(warehouse: list[Package],
             max_amount: int, max_price: int) -> list[Package]:
    if warehouse == []:
        return []

    sold = []
    temp_price = 0.0
    temp_ammount = 0.0
    average = 0
    part = 0
    count = 0
    together = 0

    for i in range(len(warehouse)):
        ammount, price, date_ex = warehouse[i]
        temp_ammount += ammount
        temp_average = (price * ammount + together ) / temp_ammount 
        
        temp_price = temp_average
        # print(temp_average)
        if temp_average > max_price or temp_ammount > max_amount:
            # print(average, "jebalo",)
            temp_ammount -= ammount
            temp_price = average
            part = i
            
            # print(average,'a')
            if average + (price / (temp_ammount + 1)) > max_price :
                # print(sold, 'jebe?', average)
                for _ in range(count):
                        warehouse.pop()
                # print("sold1", sold)
                return sold
            break
        average = temp_average
        together += price * ammount
        sold.append(warehouse[i])

        count += 1
        if i == 0:
            print('sold2', sold)
            return sold

    for _ in range(count):
        warehouse.pop()

    ammount, price, date_ex = warehouse[part]
    # print(ammount, average, 'kek')
    # if average + (price / (temp_ammount + 1)) > max_price :
    #     # print(sold, 'jebe?', average)
    #     print('sold3', sold)
    #     return sold
    
    lnght = ammount // 2
    temp_low = 0
    temp_max = ammount
    
    temp_price = (price + together) / (temp_ammount + 1)
    whole_pack = (price * ammount + together) / (temp_ammount + ammount)
    if temp_price > max_price:
        return sold
    if whole_pack < max_price:
        sold.append((ammount, price, date_ex))
        warehouse.pop()
        # print('picovina')
        return sold

    # print( temp_price, temp_ammount, price, 'mil', average)
    while temp_ammount > 0:
        # print(temp_price,"aaaaaaahhhhhhhhhh")

        # print(temp_max, lnght, temp_low)\
        find_ammount = temp_ammount + lnght
        temp_price = (price * lnght + together ) / find_ammount 
        # print(price, lnght, together, ' / ', find_ammount)
        # print(temp_ammount, lnght)
        # print(temp_price, 'tp1')
        if temp_price < max_price :
            if ((lnght + 1) * price + together) / (find_ammount + 1) > max_price:
                # print('pica')
                break
            temp_low = lnght
            half = (temp_max - temp_low) // 2
            lnght = temp_low + half
            # print('lower')
            if temp_low == lnght:
                # print('kokot low', temp_max, lnght, temp_low)
                break

        elif temp_price > max_price :
            # print('higher')
            temp_max = lnght
            half = (temp_max - temp_low) // 2
            lnght = temp_max - half
            if temp_max == lnght:
                # print('kokot max', temp_max, lnght, temp_low)
                break
        else:
            # print('picus')
            break



    sold.append((lnght, price, date_ex))
    left_ammmount = ammount - lnght
    warehouse[-1] = (left_ammmount, price, date_ex) 
    # print()
    # print('sold4', sold)
    return sold
store = [(1396609550, 32329, 84061202), (1624321554, 60840, 19870925), (46, 3478450628, 18901225)]
print(try_sell(store, 1624321600, 60939), 'should be (1624321554, 60840, 19870925), (46, 3478450628, 18901225)')
print(store, 'should be [(1396609550, 32329, 84061202)]')


def main() -> None:
    pkgD = (200, 158, 20771023)
    pkgC = (90, 14, 20220202)
    pkgB = (100, 17, 20220202)
    pkgA = (42, 9, 20211111)
    pkgs = [pkgD, pkgC, pkgB, pkgA]

    store = pkgs.copy()
    assert try_sell(store, 500, 9) == [pkgA]
    assert store == [pkgD, pkgC, pkgB]

    store = pkgs.copy()
    assert try_sell(store, 500, 12) == [pkgA, (25, 17, 20220202)]
    assert store == [pkgD, pkgC, (75, 17, 20220202)]

    store = pkgs.copy()
    assert try_sell(store, 500, 14) == [pkgA, (70, 17, 20220202)]
    assert store == [pkgD, pkgC, (30, 17, 20220202)]

    store = pkgs.copy()
    assert try_sell(store, 500, 15) == [pkgA, pkgB, pkgC]
    assert store == [pkgD]

    store = pkgs.copy()
    assert try_sell(store, 500, 16) == [pkgA, pkgB, pkgC, (2, 158, 20771023)]
    assert store == [(198, 158, 20771023)]

    store = pkgs.copy()
    assert try_sell(store, 500, 81) == [pkgA, pkgB, pkgC, pkgD]
    assert store == []
    store = [(1396609550, 32329, 84061202), (1624321554, 60840, 19870925), (46, 3478450628, 18901225)]
    print(try_sell(store, 1624321600, 60939), "should be [(1396609550, 32329, 84061202)]")
    assert try_sell(store, 1624321600, 60939) == [(1396609550, 32329, 84061202)]


if __name__ == '__main__':
    main()
