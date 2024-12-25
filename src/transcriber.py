import os
import wave

import librosa
import numpy as np
from librosa import display
import noisereduce as nr

class Scale_Identification():
    def __init__(self):
        self.NoteNameList = {
            # 0:"C",
            # 1:"C#",
            # 2:"D",
            # 3:"D#",
            # 4:"E",
            # 5:"F",
            # 6:"F#",
            # 7:"G",
            # 8:"G#",
            # 9:"A",
            # 10:"A#",
            # 11:"B",
            0:"ド",
            1:"ド#",
            2:"レ",
            3:"レ#",
            4:"ミ",
            5:"ファ",
            6:"ファ#",
            7:"ソ",
            8:"ソ#",
            9:"ラ",
            10:"ラ#",
            11:"シ",
        }
        self.path = "../music_sources/myscore/edelweiss.wav"

    def ReadFile(self):
        waveFile = wave.open(self.path)
        self.wav , self.sr = librosa.load(self.path,sr=waveFile.getframerate(),mono=True)

    def Molding(self,temp):
        return np.fliplr(temp.T)

    def NoteIdentification(self):
        chromagram = librosa.feature.chroma_stft(y=self.wav,sr=self.sr)
        chrom = self.Molding(chromagram)
        chrom = np.array(chrom)
        ResultNote = []
        max_index = len(chrom) #cheak the size of list
        for i in range(0,max_index-1):
            index = int(np.where(chrom[i] == 1)[0])
            ResultNote.append(self.NoteNameList[11-index])
        return ResultNote

    def NoteLenghtIndetification(self):
        wav_denoised = nr.reduce_noise(y=self.wav, sr=self.sr)

        onset_env = librosa.onset.onset_strength(y=wav_denoised, sr=self.sr)

        tempo, _ = librosa.beat.beat_track(onset_envelope=onset_env, sr=self.sr)

        quarter = 60/tempo

        self.notelength = {
            "whole":quarter*4,
            "half":quarter*2,
            "quarter":quarter,
            "eighth":quarter/2,
            "sixteenth":quarter/4
        }
        print(len(onset_env))
        return self.notelength

    def a(self,note):
        temp = []
        ignoreframe = self.notelength["sixteenth"]*self.sr/512
        print(ignoreframe)
        j = 0
        for i in range(1,len(note)-1):
            if (note[i-1] == note[i]):
                j = j + 1
            elif (note[i-1] != note[i]):
                if(j > ignoreframe):
                    temp.append(note[i-1])
                    j = 0
        if(j > ignoreframe):
            temp.append(note[len(note)-1])
        return temp
        
def main():
    scaledefine = Scale_Identification()
    scaledefine.ReadFile()
    result1 = scaledefine.NoteIdentification()
    print(result1)
    result2 = scaledefine.NoteLenghtIndetification()
    print(result)
    temp = scaledefine.a(result1)
    print(temp)

if __name__ == "__main__":
    main()