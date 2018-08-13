#!/usr/bin/env python3


def main():
    user_input = input()
    user_input = user_input.split()

    # N = no_of_shopping centres
    N = int(user_input[0])

    # M = no_of_roads
    M = int(user_input[1])

    # K = no_of_types_fish
    K = int(user_input[2])

    # Get no of species of fish sold by fishmonger 'T' 'eg 2 types'
    # Get species of fish sold by fishmonger 'A' 'eg carp, cod'
    T = []  # 1  1  1  1  1
    A = []  # 1  2  3  4  5
    for i in range(0, K):
        user_input = input()
        user_input = user_input.split()
        T.append(user_input[0])
        A.append(user_input[1])

    # Get shopping centre connections 'X','Y' and travel times 'Z'
    X = []  # 1  1  2  3  4
    Y = []  # 2  3  4  5  5
    Z = []  # 10 10 10 10 10
    for i in range(0, N):
        user_input = input()
        user_input = user_input.split()
        X.append(user_input[0])
        Y.append(user_input[1])
        Z.append(user_input[2])

    # Setup shopping list
    shopping_list = [1]  # 1  2  3  4  5
    for i in range(0, K):
        shopping_list.append(i + 1)

    # Set up shopping baskets
    shopping_basket = [1]
    time_1 = 0
    route_1 = [1]
    start_1 = [i for i, n in enumerate(X) if n == '1'][0]  # Position
    end_1 = 0

    time_2 = 0
    route_2 = [1]
    start_2 = [i for i, n in enumerate(X) if n == '1'][1]  # Position
    start_2 = int(start_2)
    end_2 = 0

    while set(shopping_basket) < set(shopping_list):
        if end_1 != 5:
            end_1 = int(Y[start_1])
            purchase = int(A[end_1-1])
            shopping_basket.append(purchase)
            shopping_basket.sort()
            route_1.append(int(Y[start_1]))
            time_1 += int(Z[start_1])
            start_1 = end_1
        else:
            break

    while set(shopping_basket) < set(shopping_list):
        if end_2 != 5:
            end_2 = int(Y[start_2])
            purchase = int(A[end_2-1])
            shopping_basket.append(purchase)
            shopping_basket.sort()
            route_2.append(int(Y[start_2]))
            time_2 += int(Z[start_2])
            start_2 = end_2
        else:
            break

    answer = max(time_1, time_2)
    return answer


if __name__ == '__main__':
    answer = main()
    print(answer)
