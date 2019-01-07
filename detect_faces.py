import face_recognition
import argparse
import os
import sys


def run_testData(pathToFiles, listOfFiles, outputFile):
    images = []
    for file in listOfFiles:
        images.append(face_recognition.load_image_file(os.path.join(pathToFiles, file.strip())))
    for image in images:
        locations = face_recognition.face_locations(image, number_of_times_to_upsample=10, model='cnn')
        if len(locations) > 0:
            #print('Face found')
            outputFile.write('1.000\n')
        else:
            #print('Face not found')
            outputFile.write('0.000\n')
        break

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='detect_faces.py')
    parser.add_argument('-pathToFiles', required=True,
                        help='Path to the files which should be processed')
    parser.add_argument('-outputFile', required=True,
                        help='File which should contain the output')
    parser.add_argument('-testFiles', default=None,
                        help='File which contains pair for testing')
    opt = parser.parse_args()

    with open(opt.outputFile, 'a') as fileOutput:
        with open(opt.testFiles, 'r') as fileTestpairs:
            run_testData(opt.pathToFiles, fileTestpairs, fileOutput)


