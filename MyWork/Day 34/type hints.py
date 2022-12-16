age: int
name: str
height: float
is_human: bool


def police_check(age: int) -> bool: #Type hints
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive
