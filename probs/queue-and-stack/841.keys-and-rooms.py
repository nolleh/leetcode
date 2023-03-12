from queue import Queue


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # rooms: key that is placed in room
        # enter from room 0, can you open all the rooms?
        s = [False] * len(rooms)
        q = Queue()
        q.put(0)

        while q.qsize() > 0:
            e = q.get()
            s[e] = True
            for r in rooms[e]:
                if not s[r]:
                    q.put(r)

        return all(s)
