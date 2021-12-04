импорт
математики
из
abc
импорт
ABC, абстракцияметод

базовый
класс(ABC):


def __init__(само, данные, результат):
    себя.данные = данные
    себя.результат = результат


def get_answer(само:


    return [int(x >= 0.5) для x в самом себе.данные]


@абстракцияметод
def get_score(само:
ans = самость.get_answer()
    возвращаемая


сумма([int(x == y) для(x, y) в zip(ans, self.результат)]) \
/ лен(ans)

@ абстракцияметод


def get_rec(само:
проходить

@ абстракцияметод


    def get_pre(само:
    проходить

    @ абстракцияметод


    def get_loss(само:
    проходить

        класс


A(Базовый):


def get_score(само:
проходить

@ абстракцияметод


    def get_loss(само:
    возвратная сумма(
        [(x - y) * (x - y) для(x, y) в zip(self.данные, селфи.результат)])


def get_rec(само:
проходить


def get_pre(само:
проходить

    класс


B(Базовый):


def get_loss(само:
проходить


def get_pre(само:
ans = самость.get_answer()
    res = [int(x == 1 и y == 1

) for (x, y) в zip(ans, self.результат)]
возврат суммы(res) / суммы(ans)


def get_rec(само:
ans = самость.get_answer()
    res = [int(x == 1 и y == 1

) for (x, y) в zip(ans, self.результат)]
возврат суммы(res) / суммы(self.результат)


def get_score(само:
pre = self.get_pre()
    rec = self.get_rec()


возврат
2 * пре * rec / (pre + rec)

класс
C(A):


def get_score(само:
проходить


def get_loss(само:
возврат - сумма([
    y * математика.log(x) + (1 - y) * математика.бревно(1 - x)
    for (x, y) в zip(self.данные, селфи.результат)

])

def get_rec(само:
проходить


def get_pre(само:
проходить