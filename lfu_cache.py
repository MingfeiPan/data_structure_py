#leetcode 460
class LFUCache:

    def __init__(self, capacity: int):

        self.dict = {}
        self.count_dict = {}
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:

        #if exists
        if self.dict.get(key, None):

            value, count = self.dict[key]
            self.dict[key] = (value, count + 1)

            self.count_dict[count].remove(key)
            if len(self.count_dict[count]) == 0:
                self.count_dict.pop(count)
            if self.count_dict.get(count + 1, None):
                self.count_dict[count + 1].append(key)
            else:
                self.count_dict[count + 1] = [key]
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if self.capacity == 0:
            return -1

        #if exists
        if self.dict.get(key, None):
            _, old_count = self.dict[key]

            self.count_dict[old_count].remove(key)
            if len(self.count_dict[old_count]) == 0:
                self.count_dict.pop(old_count)
            if self.count_dict.get(old_count+1, None):
                self.count_dict[old_count+1].append(key)
            else:
                self.count_dict[old_count+1] = [key]
            self.dict[key] = (value, old_count+1)
        else:
            if self.size < self.capacity:
                self.dict[key] = (value, 1)
                if self.count_dict.get(1, None):
                    self.count_dict[1].append(key)
                else:
                    self.count_dict[1] = [key]
                self.size += 1
            else:
                #make room
                cur_index = min(self.count_dict.keys())
                if len(self.count_dict[cur_index]) == 1:
                    cur_key = self.count_dict[cur_index][0]
                    self.count_dict.pop(cur_index)
                    self.dict.pop(cur_key)
                else:
                    cur_key = self.count_dict[cur_index].pop(0)
                    self.dict.pop(cur_key)


                self.dict[key] = (value, 1)
                if self.count_dict.get(1, None):
                    self.count_dict[1].append(key)
                else:
                    self.count_dict[1] = [key]               


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
