class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players.sort()
        trainers.sort()
        num_player = len(players) - 1
        num_trainer = len(trainers) - 1
        ans, np, nt = 0, 0, 0

        while np <= num_player and nt <= num_trainer:
            if players[np] <= trainers[nt]:
                np += 1
                nt += 1
                ans += 1
            elif players[np] > trainers[nt]:
                nt += 1
            else:
                np += 1
        return ans