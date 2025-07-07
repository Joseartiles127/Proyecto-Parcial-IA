import math

class BehaviorNode:
    def run(self, agent, player):
        raise NotImplementedError()

class Selector(BehaviorNode):
    def __init__(self, children):
        self.children = children

    def run(self, agent, player):
        for child in self.children:
            if child.run(agent, player):
                return True
        return False

class Sequence(BehaviorNode):
    def __init__(self, children):
        self.children = children

    def run(self, agent, player):
        for child in self.children:
            if not child.run(agent, player):
                return False
        return True

# Hojas del árbol
class IsPlayerNear(BehaviorNode):
    def run(self, agent, player):
        distance = math.hypot(player.rect.centerx - agent.rect.centerx,
                              player.rect.centery - agent.rect.centery)
        return distance < 50  # distancia para atacar

class IsPlayerVisible(BehaviorNode):
    def run(self, agent, player):
        distance = math.hypot(player.rect.centerx - agent.rect.centerx,
                              player.rect.centery - agent.rect.centery)
        return distance < 200  # distancia para persecución

class AttackPlayer(BehaviorNode):
    def run(self, agent, player):
        print("⚔️ Zombi ataca")
        agent.attack(player)
        return True

class ChasePlayer(BehaviorNode):
    def run(self, agent, player):
        agent.chase(player)
        return True

class PatrolArea(BehaviorNode):
    def run(self, agent, player):
        agent.patrol()
        return True
