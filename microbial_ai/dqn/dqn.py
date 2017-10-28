import random
import numpy as np
from collections import deque
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

class DQNAgent:
    def __init__(self, input_size, output_size):
        self._input_size = input_size
        self._output_size = output_size
        self.memory = deque(maxlen=2000)
        self._parameters = {'gamma': 0.95, 'epsilon': 1.0, 'epsilon_min': 0.01,
                             'epsilon_decay': 0.995, 'learning_rate': 0.001}
        self._model = self._build_model()

    def _build_model(self):
        model = Sequential()
        model.add(Dense(24, input_dim=self._input_size, activation='relu'))
        model.add(Dense(24, activation='relu'))
        model.add(Dense(self._output_size, activation='linear'))
        model.compile(loss='mse', optimizer=Adam(lr=self._parameters['learning_rate']))
        return model

    def act(self, state):
        if np.random.rand() <= self._parameters['epsilon']:
            return random.randrange(self._output_size)
        action_value = self._model.predict(state)
        return np.argmax(action_value[0])

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def replay(self, batch_size):
        minibatch = random.sample(self.memory, batch_size)
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                target = (reward + self._parameters['gamma'] *
                          np.amax(self._model.predict(next_state)[0]))
            target_f = self._model.predict(state)
            target_f[0][action] = target
            self._model.fit(state, target_f, epochs=1, verbose=0)
        if self._parameters['epsilon'] > self._parameters['epsilon_min']:
            self._parameters['epsilon'] *= self._parameters['epsilon_decay']
