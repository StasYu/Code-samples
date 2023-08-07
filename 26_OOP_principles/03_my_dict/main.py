class MyDict(dict):

    def get(self, __key):
        for i_key, i_value in self.items():
            if i_key == __key:
                return i_value
            else:
                return 0

new_dict = MyDict()
new_dict[1] = 1
new_dict[2] = 2
print(new_dict.get(4))

