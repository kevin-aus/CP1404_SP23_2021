class User:
    def __init__(self, name='Unknown', num_of_tacos=5, score=0):
        self.name = name
        self.num_of_tacos = num_of_tacos
        self.score = score

    def __str__(self):
        return '{}, {} points, {} tacos left' \
            .format(self.name, self.score, self.num_of_tacos)

    def give_a_taco(self, user):
        if self.num_of_tacos > 0:
            self.num_of_tacos -= 1
            user.num_of_tacos += 1
        else:
            print('No tacos to give away.')


if __name__ == '__main__':
    user1 = User('Cue', 0, 4)
    user2 = User('Amandeep', 5, 5)
    user3 = User('Anand', 5, 5)
    print(user1)
    print(user2)
    print(user3)
    user2.give_a_taco(user1)
    print(user1)
    print(user2)
