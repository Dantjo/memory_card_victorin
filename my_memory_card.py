from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QButtonGroup, QHBoxLayout, QVBoxLayout, QLabel, QRadioButton, QMessageBox, QGroupBox
from random import shuffle
from random import randint

class Question():
    def __init__(self, question, right_answer, wrong_1, wrong_2, wrong_3):
        self.question = question
        self.right_answer = right_answer
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3
question_list = []
question_list.append(Question('Какой причудой обладал Тошинори?','Один за всех','Стирание','Разрушение','Огонь и лёд'))
question_list.append(Question('Что обозначает имя "Деко"?','Беспомощный','деревянный','воинственный','я могу это сделать!!!!!!'))
question_list.append(Question('Что общего у Киришимы и ТецуТецу?','Твёрдость','Они однокласники','Умеют дышать под водой','Ничего'))
question_list.append(Question('Что случилось с отцом Изуку?','Погиб на задании','Умер от рака','Неизвестно','Ушёл к другой женщине'))
question_list.append(Question('Самый низкий ученик 1-А класса','Минета','Изуку','Бакуго','Серо'))
question_list.append(Question('Кто занял первое место на спортивном фестивале?','Бакуго','Изуку','Шото','Урарака'))
question_list.append(Question('Почему у Айзавы больные глаза?','Из-за частого использования своей причуды','Это врождённое заболеание','Врачи сами не знают','Кинескоп посадил'))
app = QApplication([])
window = QWidget()
window.setWindowTitle('MemCart')
btn_OK = QPushButton('Answer')
main_Question = QLabel('Какой национальности не существует?')
R_G_B = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Чулымцы')
rbtn_3 = QRadioButton('Смурфы')
rbtn_4 = QRadioButton('Алеуты')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
R_G_B.setLayout(layout_ans1)
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(main_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(R_G_B)
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch = 2 )
layout_line3.addStretch(1)
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addLayout(layout_line2, stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch = 1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') 
lb_Correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result)
layout_res.addWidget(lb_Correct)
AnsGroupBox.setLayout(layout_res)
layout_line1.addWidget(main_Question)
layout_line2.addWidget(R_G_B)   
layout_line2.addWidget(AnsGroupBox)  
R_G_B.hide()
layout_line3.addWidget(btn_OK, stretch=2)
def show_result():
    ''' показать панель ответов '''
    R_G_B.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
def show_question():
    ''' показать панель вопросов '''
    R_G_B.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) # сняли ограничения, чтобы можно было сбросить выбор радиокнопки
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
def test():
    if 'Ответить' == btn_OK.text():
        show_result()
    else:
        show_question()
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong_1)
    answers[2].setText(q.wrong_2)
    answers[3].setText(q.wrong_3)
    main_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()
def show_correct(res):
    lb_Result.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно,')
        window.score += 1
        print('Статистика\nВсего вопросов:', window.total,'\nПравильных ответов:', window.score)
        print('Рейтинг:',(window.score/window.total*100),'%')    
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно,')
def next_question():
    window.total += 1
    print('Статистика\nВсего вопросов:', window.total,'\nПравильных ответов:', window.score)
    cur_question = randint(0, len(question_list) - 1)
    window.cur_question = window.cur_question + 1
    if window.cur_question >= len(question_list):
        window.cur_question = 0
    q = question_list[window.cur_question]
    ask(q)
def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()
RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('MemCart')
window.cur_question = -1
btn_OK.clicked.connect(click_OK)

window.score = 0
window.total = 0

next_question()
window.resize(400, 400)

window.show()
app.exec()