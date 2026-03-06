class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()
        front = 0
        back = len(skill) - 1
        ans = 0
        cur_skill = skill[front] + skill[back]

        while front < back:
            if skill[front] + skill[back] != cur_skill:
                return -1

            else:
                ans += (skill[front] * skill[back])
                front += 1
                back -= 1
        return ans