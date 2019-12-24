import os
import sys
import shutil
import numpy as np

from ReinforcementLearning.csvRewardModel import save_reward_weights
from Utility.utility import save_model_parameters

from PyQt5.QtCore import QRunnable, pyqtSlot, QObject, pyqtSignal

def data_loader(annotation_buffer, batch):
    
    if len(annotation_buffer) < batch:
        return annotation_buffer

    else:
        index = np.random.randint(0, len(annotation_buffer), size = batch)
        train_data = [annotation_buffer[i] for i in index]  

        return train_data

class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.
    '''
    finishedSignal = pyqtSignal()

class RewardThread(QRunnable):

    def __init__(self, model):
        super(RewardThread, self).__init__()
        # Store constructor arguments (re-used for processing)
        self._signals = WorkerSignals()
        self._model = model
        self._train = True if os.listdir(self._model._weigth_path) else False
        self._done = False

    @pyqtSlot()
    def run(self):
        loss = []

        for k in range(self._model.model_parameters['K']):
            self._model.logBarSxSignal.emit("Train reward model : k-batch " + str(k) + ' of ' + str(self._model.model_parameters['K']) )
            train_clips = data_loader(self._model.annotation_buffer, self._model.reward_batch)
            loss.append(self._model.reward_model.compute_rewards(self._model.reward_model, self._model.optimizer_r, train_clips))

        self._model._iteration = 0
        self._model._model_parameters['idx'] = 0
        self._model._ann_point = 0
        #shutil.rmtree(self._model.auto_save_folder + 'annotation_buffer')
        save_model_parameters(self._model.auto_save_folder, self._model.model_parameters, self._model.iteration)
        
        save_reward_weights(self._model.reward_model, self._model.auto_save_folder)
        self._model.logBarDxSignal.emit("End train reward model, the loss is : {:.3f}".format((sum(loss)/len(loss))))
        self._model.logBarSxSignal.emit("Press process to continue or quit application")
        self._model.processButton = True
  

        
        