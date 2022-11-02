from main import question_bank

question_number = 0
question_list = question_bank

class QuizBrain:

    def __init__(self):
        self.num = question_number
        self.q_list = question_bank

    def next_question(self):
        self.ask = input(f"{q_1.q_list[q_1.num].text} True/False: ")
        self.ans = q_1.q_list[q_1.num].answer


q_1 = QuizBrain()
# print(q_1.num)
# print(q_1.q_list)
print((q_1.q_list[q_1.num].text))
print(q_1.next_question())


while True:
    if q_1.ask == q_1.ans:
        print("good job")
    else:
        print("wrong")
    q_1.num += 1
    q_1.next_question()

# print(len(q_1.q_list))

# for i in q_1.q_list:
#     print(i.text)
#     print(i.answer)
# print(q_1.q_list[q_1.num])