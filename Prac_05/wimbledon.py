"""
CP1404 Practical
Wimbledon - Reading, Processing and Displaying data
"""
FILENAME = "wimbledon.csv"
INDEX_CHAMPIONS = 2
INDEX_COUNTRIES = 1


def main():
    records = reading_file()
    champions, countries = processing_file(records)
    displaying_file(champions, countries)


def reading_file():
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def processing_file(records):
    champions = {}
    countries = set()
    for line in records:
        try:
            champions[line[INDEX_CHAMPIONS]] += 1
        except KeyError:
            champions[line[INDEX_CHAMPIONS]] = 1
        countries.add(line[INDEX_COUNTRIES])
    return champions, countries


def displaying_file(champions, countries):
    print("These are the wimbledon champions: ")
    for name, count in champions.items():
        print(name, count)
    print("\nThese {} countries have won Wimbledon: ".format(len(countries)))
    print(", ".join(country for country in sorted(countries)))


main()

