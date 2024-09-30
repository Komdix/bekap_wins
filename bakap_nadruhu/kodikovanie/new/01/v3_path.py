from ib111 import week_01  # noqa


# Napište čistou funkci ‹largest_on_path› která vrátí největší
# číslo, na které narazíme, půjdeme-li dle níže popsaných kroků od
# kladného celého čísla ‹num› po číslo 1. Povolené kroky jsou
# následující:
#
#  • je-li ‹num› sudé, vydělíme je dvěma,
#  • je-li ‹num› liché a větší než 1, vynásobíme je třemi a_přičteme 1,
#  • je-li ‹num› rovno jedné, skončili jsme.

def largest_on_path(num):
    pass


def main():
    assert largest_on_path(1) == 1
    assert largest_on_path(19) == 88
    assert largest_on_path(20) == 20
    assert largest_on_path(27) == 9232


if __name__ == '__main__':
    main()
