import db

class Language_helper:
    def start(self):
        '''запускает меню'''
        while True:
            print('\n1. добавить новое слово'
                  '\n2. начать викторину'
                  '\n3. выйти')
            user_choice = input('выберите действие -->').strip()
            if user_choice=='1':
                self.add_new_word()
            elif user_choice=='2':
                self.start_vict()
            elif user_choice=='3':
                print('досвидания')
                break
            else:
                print('некорректный выбор')



    def add_new_word(self):
        '''добавляет новое слово'''
        new_word=input('напишите слово на английском -->').strip().lower()
        new_word_translate = input('напишите перевод этого слова -->').strip().lower()
        db.add_word(new_word, new_word_translate)
        print('слово добавлено)')
    def start_vict(self):
        '''запускает викторину'''
        score=0
        total=0
        while True:
            if db.get_random_word() is None:
                print('сначала добавьте хотя бы одно слово')
                break
            random_word=db.get_random_word()
            print(f'Переведите слово: {random_word.word}')
            user_answer = input('-->').strip().lower()
            if user_answer=='выход':

                break
            elif user_answer == random_word.translate:
                print('правильно!')
                score+=1
            else:
                print(f'неверно! правильный ответ: {random_word.translate}')
            total+=1
        if total == 0:
            print('вы не дали ни одного отввввета')
        else:
            print(f'ваш процент правильных ответов: {int(score/total*100)}%')


if __name__ == '__main__':
    l = Language_helper()
    l.start()
