from ib111 import week_04  # noqa

# 1. Popište, co dělá funkce mystery_function(nums).
# 2. Přepište funkci tak, aby dosáhla stejného výstupu pouze pomocí
#    manipulace prvků ve stávajícím seznamu (tedy bez vytváření nového
#    seznamu)
# 3. Formulujte vstupní podmínku funkce mystery_function


def mystery_function(nums):
    result = [0] * len(nums)
    i = 0
    for num in nums:
        if num % 2 == 0:
            result[i] = num // 2
            i += 1
    for num in nums:
        if num % 2 != 0:
            result[i] = num * 2
            i += 1
    return result


# Odhalte, co dělá následující funkce a zjednodušte ji.

def mysterious_shift(arr):
    result = []
    secret_code = 123456
    cipher_key = 654321

    for essential_index in range(len(arr)):
        data_point = arr[essential_index] + essential_index
        code_combination = data_point + secret_code
        decoded_element = code_combination - secret_code
        key_interaction = decoded_element * cipher_key
        final_element = key_interaction / cipher_key

        distraction_1 = secret_code * cipher_key
        distraction_2 = distraction_1 / cipher_key
        distraction_3 = distraction_2 - secret_code

        final_element += distraction_3 - distraction_3

        for _ in result:
            final_element = final_element * 1

        result.append(final_element)

    return result


def main() -> None:
    pass


if __name__ == "__main__":
    main()
