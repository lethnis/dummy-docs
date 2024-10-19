from characters import Warrior, Man


def buy():
    "Слыш купи"
    pass


def sell():
    "Слыш ты купи"
    pass


def fight_club(warrior: Warrior):
    """Сразись на арене с самым сильным воином города.

    Args:
        warrior (Warrior): Воин, которого можно отправить сражаться на арену.

    Returns:
        str: имя победителя.
    """
    enemy = Warrior()
    viewer = Man()

    enemy.sleep()
    viewer.train()
    warrior.train()

    winner = "you"
    return winner
