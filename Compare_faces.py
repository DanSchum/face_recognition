import face_recognition
import argparse
import os
import sys

def run_validData(pathToFiles, outputFile):
    similarImage = None
    similarity = sys.maxsize
    for file in os.listdir(pathToFiles):
        img1 = face_recognition.load_image_file(os.path.join(pathToFiles, file))
        img1_encoding = face_recognition.face_encodings(img1)[0]
        for fileCompare in os.listdir(pathToFiles):
            if file == fileCompare:
                continue
            img2 = face_recognition.load_image_file(os.path.join(pathToFiles, fileCompare))

            # Get the face encodings for the known images
            img2_encodings = face_recognition.face_encodings(img2)
            if len(img2_encodings) > 0:

                img2_encoding = face_recognition.face_encodings(img2)[0]

                # See how far apart the test image is from the known faces
                face_distances = face_recognition.face_distance(img1_encoding, img2_encoding)
                if face_distances < similarity:
                    similarity = face_distances
                    similarImage = fileCompare

        outputFile.write('Image: ' + str(file) + ' Similar: ' + str(similarImage) + '\n')
        break


def run_testData(pathToFiles, listFilesTuple, outputFile):
    for filesTuple in listFilesTuple:
        img1 = face_recognition.load_image_file(os.path.join(pathToFiles, filesTuple[0]))
        img2 = face_recognition.load_image_file(os.path.join(pathToFiles, filesTuple[1]))

        img1_encodings = face_recognition.face_encodings(img1)
        img2_encodings = face_recognition.face_encodings(img2)
        if len(img1_encodings) > 0 and len(img2_encodings) > 0:

            # Get the face encodings for the known images
            img1_encoding = img1_encodings[0]
            img2_encoding = img2_encodings[0]

            # See how far apart the test image is from the known faces
            face_distances = face_recognition.face_distance(img1_encoding, img2_encoding)
            outputFile.write(str(face_distances) + '\n')
        else:
            print('Face not found')
            outputFile.write('0.000\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compare_faces.py')
    parser.add_argument('-mode', required=True,
                        help='Mode')
    parser.add_argument('-pathToFiles', required=True,
                        help='Path to the files which should be processed')
    parser.add_argument('-outputFile', required=True,
                        help='File which should contain the output')
    parser.add_argument('-testPairs', default=None,
                        help='File which contains pair for testing')
    opt = parser.parse_args()

    with open(opt.outputFile, 'a') as fileOutput:
        if opt.mode == 'test':
            testPairs = []
            with open(opt.testPairs, 'r') as fileTestpairs:
                for line in fileTestpairs:
                    splits = line.split()
                    testPairs.append((splits[0], splits[1]))
                run_testData(opt.pathToFiles, testPairs, fileOutput)
        elif opt.mode == 'valid':
            run_validData(opt.pathToFiles, fileOutput)
        else:
            print('Mode not found')


