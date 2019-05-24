def __split_subtitles(self, f_name_ru_subtitles, f_name_prepared_subtitles):
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