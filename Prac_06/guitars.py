"""CP1404 - Practical - Guitars"""
from Prac_06.guitar import Guitar


def main():
    """Guitar Program that stores fields using the guitar class"""
    guitar_library = []
    guitar_library.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitar_library.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    print("my guitars!")
    name = input("Name:")
    year = int(input("Year:"))
    cost = int(input("Cost: $"))
    new_guitar = Guitar(name, year, cost)
    guitar_library.append(new_guitar)
    print(f"{new_guitar} added to the library")

    print("These are my guitars:")
    for i, guitar_library in enumerate(guitar_library, 1):
        if guitar_library.is_vintage():
            vintage_string = " (vintage)"
            print(f"Guitar {i}: {guitar_library.name:>10} ({guitar_library.year}), worth ${guitar_library.cost:5,.2f}{vintage_string}")
        else:
            print(f"Guitar {i}: {guitar_library.name} ({guitar_library.year}), worth ${guitar_library.cost:5,.2f}")


if __name__ == "__main__":
    main()
