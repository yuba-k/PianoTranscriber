import os
import wave

import librosa
import numpy as np
from librosa import display


class Scale_Identification():
    def __init__(self):
        self.NoteNameList = {
            0:"C",
            1:"C#",
            2:"D",
            3:"D#",
            4:"E",
            5:"F",
            6:"F#",
            7:"G",
            8:"G#",
            9:"A",
            10:"A#",
            11:"B",
        }
        self.path = "../music_sources/myscore/"
        self.filename = [f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path,f))]

    def ReadFile(self):
        for i in self.filename:
            waveFile = wave.open(self.path + i)
            wav , sr = librosa.load(self.path + i,sr=waveFile.getframerate())
            chromagram = librosa.feature.chroma_stft(y=wav,sr=sr)
            result = self.Identification(self.Molding(chromagram))
            print(result)

    def Molding(self,temp):
        return np.fliplr(temp.T)

    def Identification(self,chrom):
        chrom = np.array(chrom)
        ResultNote = []
        max_index = len(chrom) #cheak the size of list
        for i in range(0,max_index-1):
            index = int(np.where(chrom[i] == 1)[0])
            ResultNote.append(self.NoteNameList[11-index])
        return ResultNote
        
def main():
    scaledefine = Scale_Identification()
    scaledefine.ReadFile()

if __name__ == "__main__":
    main()