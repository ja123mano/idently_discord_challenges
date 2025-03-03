
def create_diamond(width: int) -> None:
    """
    Prints a diamond created with asterisks in the terminal.

    Parameters
    ----------
    width : int
        An integer value that represents the width (number of asterisks)
        of the most inner layer of the diamond.
    """
    
    if type(width) != int:
        raise TypeError(f"Width value '{width}' is non-Integer. Please enter an integer")

    width = abs(width)
    init_stars: int = 1
    if width % 2 == 0: init_stars = 2

    for stars in range(init_stars, width, 2):
        diff: int = width-stars
        printing_val: str = " "*(diff//2)
        printing_val += "*"*stars
        print(printing_val)

    for stars in range(width, 0, -2):
        diff: int = width-stars
        printing_val: str = " "*(diff//2)
        printing_val += "*"*stars
        print(printing_val)

    return None

if __name__ == "__main__":
    create_diamond(10)