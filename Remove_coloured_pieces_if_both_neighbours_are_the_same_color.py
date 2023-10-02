class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        def winnerOfGame(colors):
            alice_moves = 0
            bob_moves = 0

            for i in range(1, len(colors)-1):
                if colors[i-1:i+2] == "AAA":
                    alice_moves += 1
                elif colors[i-1:i+2] == "BBB":
                    bob_moves += 1

            return alice_moves > bob_moves

        result = winnerOfGame(colors)
        return result

