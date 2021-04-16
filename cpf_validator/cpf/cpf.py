import re


def is_cpf_valid(cpf):
    """ If cpf in the Brazilian format is valid, it returns True, otherwise, it returns False. """

    # Check if type is str
    if not isinstance(cpf, str):
        return False

    # Remove some unwanted characters
    cpf = re.sub("[^0-9]", '', cpf)

    # Verify if CPF number is equal
    if cpf in ('00000000000', \
         '11111111111', \
              '22222222222', \
                   '33333333333', \
                        '44444444444', \
                             '55555555555', \
                                  '66666666666', \
                                       '77777777777', \
                                            '88888888888', \
                                                 '99999999999'):
        return False

    # Checks if string has 11 characters
    if len(cpf) != 11:
        return False

    sum = 0
    weight = 10
    for number in range(9):
        sum = sum + int(cpf[number]) * weight

        # Decrement weight
        weight = weight - 1

    verifying_digit = 11 - sum % 11

    if verifying_digit > 9:
        first_verifying_digit = 0
    else:
        first_verifying_digit = verifying_digit
    sum = 0
    weight = 11
    for number in range(10):
        sum = sum + int(cpf[number]) * weight

        # Decrement weight
        weight = weight - 1

    verifying_digit = 11 - sum % 11

    if verifying_digit > 9:
        second_verifying_digit = 0
    else:
        second_verifying_digit = verifying_digit

    if cpf[-2:] == "%s%s" % (first_verifying_digit, second_verifying_digit):
        return True
    return False
