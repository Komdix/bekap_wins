from ib111 import week_07  # noqa


# V tomto domácím úkolu si naprogramujeme zjednodušenou reprezentaci akciové
# burzy. Skutečné burzy typicky umožňují zadávat různé druhy pokynů, my se však
# omezíme jen na jednoduché nákupní a prodejní pokyny. Každý pokyn vždy
# obsahuje jméno (nebo jiný identifikátor) obchodníka, který jej podal,
# množství akcií, které chce nakoupit nebo prodat, a jednotkovou cenu za akcii.
# Podle typu pokynu je jednotková cena buď maximální cena, za kterou chce
# obchodník nakupovat, nebo minimální cena, za kterou chce prodávat.
#
# Nenajde-li se k podanému pokynu odpovídající pokyn opačný, stane se z něj
# pokyn čekající. Čekající pokyny se řadí podle jednotkové ceny – přednost mají
# nákupní pokyny s vyšší cenou a prodejní pokyny s nižší cenou (tedy ty, které
# jsou blíže středu). Mezi pokyny se stejnou cenou mají přednost ty, které
# přišly na burzu dříve. Přijde-li na burzu nový pokyn, pokusí se vypořádat
# (i částečně) s existujícími opačnými pokyny. Pokud se celý nevypořádá, jeho
# zbytek se zařadí mezi pokyny čekající.
#
# Vypořádání mezi pokyny je možné, pokud je jednotková cena nákupního pokynu
# větší nebo rovna jednotkové ceně prodejního pokynu. Při vypořádání se mezi
# obchodníky převede tolik akcií, kolik je minimum z počtů v obou pokynech.
# Cena vypořádání se v realitě počítá různě. My budeme v tomto zadání používat
# vypořádání zvýhodňující později příchozího, tj. cena obchodu bude vždy dána
# cenou pokynu, který byl na burze dříve.
#
# Ukážeme si to na příkladu: Mějme akciovou společnost ACME, která na začátku
# obchodování nemá žádné čekající příkazy. Postupně budou přicházet tyto
# příkazy:
#
# 1. Strýček Skrblík chce prodat 50 akcií za cenu $120.
# 2. Rampa McKvák chce nakoupit 100 akcií za cenu $90.
# 3. Hamoun Držgrešle chce prodat 70 akcií za cenu $110.
# 4. Kačer Donald chce prodat 20 akcií za cenu $120.
#
# Žádné z těchto pokynů se zatím nevypořádají a situaci čekajících pokynů si
# můžeme znázornit takto:
#
# │ typ    │ cena │ počet │ obchodník             │
# ├────────┼─────▻┼──────▻┼◅──────────────────────┤
# │ prodej │  120 │    20 │ Kačer Donald          │
# │ prodej │  120 │    50 │ Strýček Skrblík       │
# │ prodej │  110 │    70 │ Hamoun Držgrešle      │
# │┄┄┄┄┄┄┄┄│┄┄┄┄┄┄│┄┄┄┄┄┄┄│┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄│
# │ nákup  │   90 │   100 │ Rampa McKvák          │
#
# (Nákupní pokyny píšeme dolů, prodejní pokyny nahoru, přednost mají ty pokyny,
# které jsou blíže středové čáře.)
#
# Dále přijde pokyn Paní Čvachtové, která chce koupit 90 akcií za $110.
# Tento pokyn se částečně vypořádá s pokynem Hamouna Držgrešle a paní Čvachtová
# obdrží jeho 70 akcií za cenu $110. Protože její pokyn nebyl zcela vypořádán
# a další prodejní pokyny, se kterými by se mohl vypořádat, už nejsou, zařadí
# se mezi čekající nákupní pokyny. Situace tedy vypadá takto:
#
# │ typ    │ cena │ počet │ obchodník             │
# ├────────┼─────▻┼──────▻┼◅──────────────────────┤
# │ prodej │  120 │    20 │ Kačer Donald          │
# │ prodej │  120 │    50 │ Strýček Skrblík       │
# │┄┄┄┄┄┄┄┄│┄┄┄┄┄┄│┄┄┄┄┄┄┄│┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄│
# │ nákup  │  110 │    20 │ Paní Čvachtová        │
# │ nákup  │   90 │   100 │ Rampa McKvák          │
#
# Nakonec přijde nákupní pokyn Magiky von Čáry, která chce koupit 60 akcií
# za cenu $130. Tento pokyn se nejprve vypořádá s pokynem Strýčka Skrblíka
# (má stejnou cenu jako pokyn Kačera Donalda, ale přišel na burzu dříve),
# a to za $120. Protože tím není pokyn zcela vypořádán, zbylých 10 akcií
# se za stejnou cenu zobchoduje s Kačerem Donaldem.
#
# Výsledná situace tedy vypadá takto:
#
# │ typ    │ cena │ počet │ obchodník             │
# ├────────┼─────▻┼──────▻┼◅──────────────────────┤
# │ prodej │  120 │    10 │ Kačer Donald          │
# │┄┄┄┄┄┄┄┄│┄┄┄┄┄┄│┄┄┄┄┄┄┄│┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄│
# │ nákup  │  110 │    20 │ Paní Čvachtová        │
# │ nákup  │   90 │   100 │ Rampa McKvák          │
#
# Pro rekapitulaci, postupně proběhly následující obchody:
#
# • Hamoun Držgrešle → Paní Čvachtová: 70 akcií za $110
# • Strýček Skrblík → Magika von Čáry: 50 akcií za $120
# • Kačer Donald → Magika von Čáry: 10 akcií za $120
#
# Pro reprezentaci jednotlivých transakcí máte připravenu třídu ‹Transaction›
# s těmito atributy:
#
# • ‹buyer_id› – řetězec označující jméno kupujícího;
# • ‹seller_id› – řetězec označující jméno prodávajícího;
# • ‹amount› – kladné celé číslo označující počet zobchodovaných akcií;
# • ‹price› – kladné celé číslo označující jednotkovou cenu, za kterou
#   obchod proběhl.

class Transaction:
    def __init__(self, buyer_id: str, seller_id: str,
                 amount: int, price: int):
        self.buyer_id = buyer_id
        self.seller_id = seller_id
        self.amount = amount
        self.price = price


# Třída ‹Order› reprezentuje obchodní pokyn (nákup nebo prodej); má tyto
# atributy:
#
# • ‹trader_id› – řetezěc označující obchodníka, který vydal pokyn;
# • ‹amount› – kladné celé číslo označující požadovaný počet akcií;
# • ‹price› – kladné celé číslo označující požadovanou cenu.

class Order:
    def __init__(self, trader_id: str, amount: int, price: int):
        self.trader_id = trader_id
        self.amount = amount
        self.price = price


# Třída ‹Stock› obsahuje všechny informace týkající se jedné akciové
# společnosti; má tyto atributy:
#
# • ‹history› – seznam všech transakcí (objektů typu ‹Transaction›), které
#   se s akciemi této společnosti prováděly;
# • ‹buyers› – seznam všech čekajících (dosud nevypořádaných) nákupních
#   pokynů (objektů typu ‹Order›);
# • ‹sellers› – seznam všech čekajících (dosud nevypořádaných) prodejních
#   pokynů (objektů typu ‹Order›).
#
# Seznam ‹buyers› budeme chtít udržovat vždy seřazený tak, aby pokyny s vyšší
# cenou byly blíže ke konci seznamu; pokud je více pokynů se stejnou cenou,
# pak bude blíže ke konci seznamu pokyn, který přišel dříve (pomocí procedury
# ‹place_buy_order›).
#
# Seznam ‹sellers› budeme chtít udržovat vždy seřazený tak, aby pokyny s nižší
# cenou byly blíže ke konci seznamu; pokud je více pokynů se stejnou cenou,
# pak bude blíže ke konci seznamu pokyn, který přišel dříve (pomocí procedury
# ‹place_sell_order›).
#
# «Poznámka:» Toto uspořádání zaručí, že pokyny na konci seznamu budou ty,
# které se mají vypořádat jako první, čehož můžete s výhodou využít při
# implementaci procedur ‹place_*_order›.

class Stock:
    def __init__(self) -> None:
        self.history: list[Transaction] = []
        self.buyers: list[Order] = []
        self.sellers: list[Order] = []


# Pro reprezentaci celé burzy používáme typový alias ‹StockExchange›,
# což je slovník, jehož klíči jsou zkrácená burzovní jména akciových
# společností (tzv. «ticker symbol») a hodnotami objekty typu ‹Stock›.

StockExchange = dict[str, Stock]


# Implementujte procedury ‹place_buy_order› a ‹place_sell_order›, které na
# burzu vloží nový nákupní, resp. prodejní pokyn a pokusí se jej co nejvíce
# vypořádat (viz výše). Vypořádaný pokyn (nebo jeho části) vloží na konec
# seznamu ‹history›, nevypořádaný pokyn (nebo jeho část) zařadí do
# odpovídajícího seznamu pokynů.
#
# Vstupní podmínkou obou procedur je, že ‹ticker_symbol› je validní ticker
# symbol, který je klíčem ve slovníku burzy, ‹amount› a ‹price› jsou kladná
# celá čísla a seznamy ‹buyers› a ‹sellers› jsou seřazené, jak je popsáno výše.
# Procedury implementujte tak, aby toto řazení zachovaly.

def place_buy_order(stock_exchange: StockExchange,
                    ticker_symbol: str,
                    trader_id: str,
                    amount: int, price: int) -> None:
    pass


def place_sell_order(stock_exchange: StockExchange,
                     ticker_symbol: str,
                     trader_id: str,
                     amount: int, price: int) -> None:
    pass


# V zadání je připravena procedura ‹print_stock›, která pro zadaný ticker
# symbol textově vykreslí tabulku čekajících pokynů a seznam transakcí.
# Tuto proceduru můžete využít pro ladění.


def main() -> None:
    duckburg_se: StockExchange = {'ACME': Stock()}

    place_sell_order(duckburg_se, 'ACME', 'Strýček Skrblík', 50, 120)
    place_buy_order(duckburg_se, 'ACME', 'Rampa McKvák', 100, 90)
    place_sell_order(duckburg_se, 'ACME', 'Hamoun Držgrešle', 70, 110)
    place_sell_order(duckburg_se, 'ACME', 'Kačer Donald', 20, 120)

    acme = duckburg_se['ACME']
    assert acme.history == []

    assert len(acme.buyers) == 1
    check_order(acme.buyers[0], 'Rampa McKvák', 100, 90)

    assert len(acme.sellers) == 3
    check_order(acme.sellers[0], 'Kačer Donald', 20, 120)
    check_order(acme.sellers[1], 'Strýček Skrblík', 50, 120)
    check_order(acme.sellers[2], 'Hamoun Držgrešle', 70, 110)

    place_buy_order(duckburg_se, 'ACME', 'Paní Čvachtová', 90, 110)

    assert len(acme.history) == 1
    check_transaction(acme.history[0], 'Paní Čvachtová', 'Hamoun Držgrešle',
                      70, 110)

    assert len(acme.buyers) == 2
    check_order(acme.buyers[0], 'Rampa McKvák', 100, 90)
    check_order(acme.buyers[1], 'Paní Čvachtová', 20, 110)

    assert len(acme.sellers) == 2
    check_order(acme.sellers[0], 'Kačer Donald', 20, 120)
    check_order(acme.sellers[1], 'Strýček Skrblík', 50, 120)

    place_buy_order(duckburg_se, 'ACME', 'Magika von Čáry', 60, 130)

    assert len(acme.history) == 3
    check_transaction(acme.history[0], 'Paní Čvachtová', 'Hamoun Držgrešle',
                      70, 110)
    check_transaction(acme.history[1], 'Magika von Čáry', 'Strýček Skrblík',
                      50, 120)
    check_transaction(acme.history[2], 'Magika von Čáry', 'Kačer Donald',
                      10, 120)

    assert len(acme.buyers) == 2
    check_order(acme.buyers[0], 'Rampa McKvák', 100, 90)
    check_order(acme.buyers[1], 'Paní Čvachtová', 20, 110)

    assert len(acme.sellers) == 1
    check_order(acme.sellers[0], 'Kačer Donald', 10, 120)


def check_order(order: Order, trader_id: str, amount: int, price: int) -> None:
    assert order.trader_id == trader_id
    assert order.amount == amount
    assert order.price == price


def check_transaction(transaction: Transaction, buyer_id: str, seller_id: str,
                      amount: int, price: int) -> None:
    assert transaction.buyer_id == buyer_id
    assert transaction.seller_id == seller_id
    assert transaction.amount == amount
    assert transaction.price == price


def print_rj(pos_num: int, size: int) -> None:
    digits = 1
    num = pos_num
    while num > 9:
        num //= 10
        digits += 1
    for _ in range(size - digits):
        print(" ", end="")
    print(pos_num, end="")


def print_order(order: Order) -> None:
    print_rj(order.price, 10)
    print_rj(order.amount, 7)
    print(" (", order.trader_id, ")", sep="")


def print_stock(stock_exchange: StockExchange, ticker_symbol: str) -> None:
    assert ticker_symbol in stock_exchange

    stock = stock_exchange[ticker_symbol]
    print("===", ticker_symbol, "===")
    print("     price amount  trader")
    print("  -------------------------------------------------------------")

    for order in stock.sellers:
        print_order(order)
    print("  -------------------------------------------------------------")

    for i in range(len(stock.buyers) - 1, -1, -1):
        print_order(stock.buyers[i])
    print("  -------------------------------------------------------------")

    for transaction in stock.history:
        print("    ",
              transaction.seller_id, " -> ", transaction.buyer_id, ": ",
              transaction.amount, " at ", transaction.price, sep="")


if __name__ == '__main__':
    main()
