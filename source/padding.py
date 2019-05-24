def __tokenizer(self, str):
        ''' Разбиение строки на слова. '''
        result = re.split(r'(\W)', str) # разбиение строки на последовательность из слов и знаков препинания
        result = [ word for word in result if word.strip() ] # удаление пустых элементов из последовательности
        if len(result) > 1:
            if result[-1] == '.': # удаление точки в конце, если она есть
                del result[-1]
        return result


    def __fill_cells(self, data):
        ''' Выравнивание всех пар по размеру. '''
        result = [ [self.__fill_cells_quest(q), self.__fill_cells_answ(a)] for [q,a] in data ]
        return result


    def __fill_cells_answ(self, a):
        ''' Выравнивание ответа по размеру, заполняя пустые места словом <PAD>. Например: [..., '<EOS>', '<PAD>', ...] '''
        result = a + ['<EOS>'] + ['<PAD>'] * (self.input_size - len(a) - 1) 
        return result


    def __fill_cells_quest(self, q):
        ''' Выравнивание вопроса по размеру, заполняя пустые места словом <PAD>. Например: [..., '<PAD>', 'вопрос', '<GO>'] '''
        result = ['<PAD>'] * (self.input_size - len(q) - 1) + q + ['<GO>']
        return result