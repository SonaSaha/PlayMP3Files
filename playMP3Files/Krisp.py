import os
import argparse
import playsound
import json

# Takes directory name where is stored mp3 audio files and plays them
# returns dictionary: file name as kay, the value is c/n depends the audio was clean or noisy
def PlayMP3Files(directoryName):

    mp3Files = os.listdir(directoryName)
    result = {}
    for f in mp3Files:
        playsound.playsound(f"{directoryName}/{f}")
        result[f] = input("Enter the audio was noisy(n) or clean(c)!")
    return result

# Takes dictionary as argument and converts it to json string writing it in the file
# returns the new created file
def convertDictionaryToJSONFile(MP3dictionary):

    with open('resultAsJson.txt', 'w+') as resultAsJson:
        json.dump(MP3dictionary, resultAsJson)

    return resultAsJson


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dirName', type=str, help='The directory name')
    args = parser.parse_args()
    resultDict = PlayMP3Files(args.dirName)
    convertDictionaryToJSONFile(resultDict)