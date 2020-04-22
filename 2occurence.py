
class SecondTask():
    def func(self, text, first, second):
        text = text.split(' ')
        res = []
        for i in range(len(text) - 2):
            if text[i] == first and text[i+1] == second:
                res.append(text[i+2])
        return res


sec_task = SecondTask()
#print(sec_task.func("we will we will rock you", first = "we", second = "will"))
print(sec_task.func('alice is a good girl she is a good student', 'a', 'good'))
