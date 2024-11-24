import random

# Определяем значения карт
values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}


# Класс карты
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"


# Класс колоды карт
class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades'] for value in
                      values.keys()]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop() if self.cards else None


# Класс игрока
class Player:
    def __init__(self):
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def calculate_hand_value(self):
        value = sum(values[card.value] for card in self.hand)
        # Корректируем значение тузов
        aces = sum(1 for card in self.hand if card.value == 'A')
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value

    def __str__(self):
        return ', '.join(str(card) for card in self.hand)


# Основная логика игры
def play_blackjack():
    print("Добро пожаловать в Блэк Джек!")

    deck = Deck()
    player = Player()
    dealer = Player()

    # Раздача начальных карт
    for _ in range(2):
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())

    # Игрок делает ход
    while True:
        print(f"\nВаши карты: {player} (Сумма: {player.calculate_hand_value()})")
        print(f"Карты дилера: {dealer.hand[0]}, ?")

        if player.calculate_hand_value() == 21:
            print("У вас Блэк Джек! Вы выиграли!")
            return

        action = input("Хотите взять карту? (y/n): ").strip().lower()
        if action == 'y':
            player.add_card(deck.deal_card())
            if player.calculate_hand_value() > 21:
                print(f"\nВаши карты: {player} (Сумма: {player.calculate_hand_value()})")
                print("Вы превысили 21! Вы проиграли.")
                return
        else:
            break

    # Ход дилера
    while dealer.calculate_hand_value() < 17:
        dealer.add_card(deck.deal_card())

    # Показываем результаты
    print(f"\nВаши карты: {player} (Сумма: {player.calculate_hand_value()})")
    print(f"Карты дилера: {dealer} (Сумма: {dealer.calculate_hand_value()})")

    if dealer.calculate_hand_value() > 21:
        print("Дилер превысил 21! Вы выиграли!")
    elif player.calculate_hand_value() > dealer.calculate_hand_value():
        print("Вы выиграли!")
    elif player.calculate_hand_value() < dealer.calculate_hand_value():
        print("Вы проиграли!")
    else:
        print("Ничья!")


if __name__ == "__main__":
    play_blackjack()