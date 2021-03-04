def main():
    for fb in range(1, 101):
        if fb % 3 == 0:
            print("fizz")
            continue
        elif fb % 5 == 0:
            print("buzz")
            continue
        elif fb % 3 == 0 and fb % 5 == 0:
            print("fizzbuzz")
            continue
        print(fb)

main()