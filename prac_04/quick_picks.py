def main():
    import random

    MIN_NUMBER = 1
    MAX_NUMBER = 45
    NUM_PER_QUICK_PICK = 6

    def generate_quick_pick():
        numbers = random.sample(range(MIN_NUMBER, MAX_NUMBER + 1), NUM_PER_QUICK_PICK)
        #Not include 45, so add 1
        numbers.sort()
        return numbers

    def generate_and_print_quick_picks(num_quick_picks):
        for _ in range(num_quick_picks):
            quick_pick = generate_quick_pick()
            print(' '.join(map(str, quick_pick)))

    num_quick_picks = int(input("How many quick picks? "))

    generate_and_print_quick_picks(num_quick_picks)


main()