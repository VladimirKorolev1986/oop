def check_card_number(number: str):
    """Формат номера следующий: XXXX-XXXX-XXXX-XXXX, где X - лю бая цифра (от 0 до 9)."""
    if len(number.split('-')) != 4:
        return False
    if not any([x.isdigit() for x in number.split('-')]):
        return False
    return True


sstr = '1234-5678-9876-0987'

print(check_card_number(sstr))
