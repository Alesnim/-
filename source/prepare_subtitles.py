def __split_subtitles(self, f_name_ru_subtitles, f_name_prepared_subtitles):
        ''' Считывание очищенных субтитров из f_name_ru_subtitles, разбиение предложений из них на слова, построение гистограммы размеров предложений
        и сохранение в f_name_prepared_subtitles.
        1. f_name_ru_subtitles - имя .txt файла с очищенными субтитрами
        2. f_name_prepared_subtitles - имя .pkl файла с обработанными субтитрами '''

        print('[i] Считывание очищенных субтитров из %s' % f_name_ru_subtitles)
        with open(f_name_ru_subtitles, 'r') as f_ru_subtitles:
            subtitles = f_ru_subtitles.readlines()

        print('[i] Разбиение предложений из субтитров на отдельные слова... ')
        i = 0
        subtitles_words = []
        while i < len(subtitles):
            if i % 1000 == 0 or i == len(subtitles) - 1:
                os.write(sys.stdout.fileno(), curses.tigetstr('cuu1'))
                print('[i] Разбиение предложений из субтитров на отдельные слова... %i из %i' % (i, len(subtitles)))
            words = re.split(r'(\W)', subtitles[i]) # разбиение строки на последовательность из слов и знаков препинания
            words = [ word for word in words if word.strip() ] # удаление пустых элементов из последовательности
            if len(words) < 135:
                subtitles_words.append(words)
            i += 1

        self.max_sequence_length = (np.asarray([ len(words) for words in subtitles_words ])).max()
        print('[i] Максимальная длина предложения: ' + str(self.max_sequence_length))
        
        print('[i] Сохранение предобработанных субтитров в %s' % f_name_prepared_subtitles)
        with open(f_name_prepared_subtitles, 'wb') as file:
            pickle.dump(subtitles_words, file)

        self.__build_histogram(subtitles_words)