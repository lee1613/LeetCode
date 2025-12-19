class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
            return self.parent[i]
        return i

    def unite(self, i, j):
        parent_i = self.find(i)
        parent_j = self.find(j)
        self.parent[parent_i] = parent_j

    def in_same_set(self, i, j):
        if self.find(i) == self.find(j):
            return True
        return False

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # Sort it with the timeline, for those in the same time line, they all should be added to the list if one of them knows the secret, using the set to check if a person knows the secret
        res = {0, firstPerson}

        meetings.sort(key = lambda x: x[2])

        ufds = UnionFind(n)
        ufds.unite(firstPerson, 0)
        curr = meetings[0][2]
        # need ppl to take note which person to check for whom have meeting at this time point
        ppl = set()
        for xi, yi, time in meetings:
            if time == curr:
                ufds.unite(xi, yi)
                ppl.add(xi)
                ppl.add(yi)
                
            # At the time where a meeting have a different time from the previous meetings, we compile all of them. This means that at the end of the loop there'll be a time we need to compile all of them again
            else:
                # Change the curr to time if they are different
                curr = time
                # Shared variable to indicate that all of the person in the current timeframe have shared the secret, note that not all the person in the curr time frame knows the secret, only the one in contact with the one knows. Is there a way to process such that the person who knows will be prioritize

                # I'm thinking of a way to sort the person who don't know anything, so later those people who have access to the secret has something to share, could be checked. A data structure that could classifiy those having the same intersection together under a head (It's called Union Find Disjoint Set)

                ## Looping through every single person to check of having secret then looping again everyone to check if it's the same set is annoying, maybe there's a way to determine who should be prioritize? Just use the secred_holder to take note of the person who knows the secret
                for person in ppl:
                    # Because the root is in itself
                    if ufds.in_same_set(person, 0):
                        res.add(person)
                    else:
                        ufds.parent[person] = person
                # Create a new UFDS at the end of it, and reset the ppl to be counted
                ufds.unite(xi, yi)
                ppl = set()
                ppl.add(xi)
                ppl.add(yi)        
        
        for person in ppl:
            if ufds.in_same_set(person, 0):
                res.add(person)
            else:
                ufds.parent[person] = person
        
        return list(res)
