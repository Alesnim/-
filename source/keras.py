import os


ad = Adam(lr=0.00005) 

input_context = Input(shape=(maxlen_input,), dtype=np.int32, name='input_context')
input_answer = Input(shape=(maxlen_input,), dtype=np.int32, name='input_answer')
LSTM_encoder = LSTM(sentence_embedding_size, init= 'lecun_uniform')
LSTM_decoder = LSTM(sentence_embedding_size, init= 'lecun_uniform')
if os.path.isfile(weights_file):
    Shared_Embedding = Embedding(output_dim=word_embedding_size, 
                                 input_dim=dictionary_size, input_length=maxlen_input)
else:
    Shared_Embedding = Embedding(output_dim=word_embedding_size,
                                 input_dim=dictionary_size, weights=[embedding_matrix],
                                 input_length=maxlen_input)
word_embedding_context = Shared_Embedding(input_context)
context_embedding = LSTM_encoder(word_embedding_context)

word_embedding_answer = Shared_Embedding(input_answer)
answer_embedding = LSTM_decoder(word_embedding_answer)

merge_layer = concatenate([context_embedding, answer_embedding], axis=1)
out = Dense(dictionary_size//2, activation="relu", )(merge_layer)
out = Dense(dictionary_size, activation="softmax")(out)

model = Model(input=[input_context, input_answer], output = [out])

model.compile(loss='categorical_crossentropy', optimizer=ad)