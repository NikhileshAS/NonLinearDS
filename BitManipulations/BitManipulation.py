def setBit(num: int, position: int) -> int:
    return num | 1 << position


def getBit(num: int, position: int) -> bool:
    return (num & (1 << position)) != 0


def clearBit(num: int, position: int) -> int:
    return num & ~(1 << position)


def clearBitsThroughI(num: int, position: int) -> int:
    return num & ((1 << position) - 1)


def clearBitsIThrough0(num: int, i: int) -> int:
    return num & (-1 << (i+1))


def updateBit(num: int, position: int, bit: bool) -> int:
    return num & ~(1 << position) | ((1 if bit else 0) << position)


def main():
    print(setBit(16, 4))
    print(1 if getBit(16, 4) else 0)
    print(clearBit(10, 3))
    print(clearBitsThroughI(16, 3))
    print(clearBitsIThrough0(10, 2))


if __name__ == '__main__':
    main()

