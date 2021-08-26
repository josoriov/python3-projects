from animals import *

zoo = {
    1: camel,
    2: lion,
    3: deer,
    4: goose,
    5: bat,
    6: rabbit
}


def main():
    run: bool = True
    while run:
        cage: str = input("Select the cage you wish to see:\n")
        if cage == "exit":
            print("\nSee you!\n")
            break
        cage_num: int = int(cage)
        animal: str = zoo.get(cage_num, "")
        text = f"\nThe inputted cage ({cage}) is not registered\n" if len(animal) == 0 else animal
        print(text)


if __name__ == '__main__':
    main()
