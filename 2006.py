
T = int(input())


guesses = list(map(int, input().split()))


correct_guesses = guesses.count(T)


print(correct_guesses)
