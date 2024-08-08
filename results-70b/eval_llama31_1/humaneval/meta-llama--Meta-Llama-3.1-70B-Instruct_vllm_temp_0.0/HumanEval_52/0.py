def below_threshold(l: list, t: int) -> bool:
    return all(i < t for i in l)