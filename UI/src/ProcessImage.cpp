#include <iostream>
#include <fstream>
#include <stdlib.h>
#include "../include/image.h"

int readImageHeader(const char[], int&, int&, int&, bool&);
int readImage(const char[], ImageType&);
int writeImage(const char[], ImageType&);
void sampling(ImageType, ImageType&, const int);

ImageType ProcessImage(const char filePath[] ) 
{
    bool type2;
    int Z, X, Y; // for image sampling
    const int FACTOR = 2; // Change this to make new size

    readImageHeader(filePath, Z, X, Y, type2);
    ImageType samplingImage(Z, X, Y);
    samplingImage.getImageInfo(Z, X, Y);

    int L = Z / FACTOR,
        O = X / FACTOR,
        P = Y;
    
    ImageType resizedImg(L, O, P);
    readImage(filePath, samplingImage);
    sampling(samplingImage, resizedImg, FACTOR);
    return resizedImg;
}

/**
 *  Details: Take in an integer defining how much to sample the
 *            image, e.g. 2. Run through the pixel values and store
 *            every 2nd pixel value into a new array which will be the
 *            pixel values of the new image, or every 4th pixel, or 8th.
 * */
void sampling(ImageType srcImg, ImageType& newImg, const int FACTOR) {
  // Variables
  int srcRows,
      srcCols,
      srcLvls;

  // New image variables
  int value;
  int actualRow = 0,
      actualCol = 0;

  //Initialization
  srcImg.getImageInfo(srcRows, srcCols, srcLvls);

  cout << " " << srcRows << " " << srcCols << "\n";

  for (int cols = 0; cols < srcCols; cols += FACTOR) {
    actualRow = 0;
    for (int rows = 0; rows < srcRows; rows += FACTOR) {
        srcImg.getPixelVal(rows, cols, value);

        // Debugging
        // cout << "ActRow: " << actualRow << " ActCol: " << actualCol << " Val: " << value << "\n";

        newImg.setPixelVal(actualRow, actualCol, value);

      actualRow++;
    }

    actualCol++;
  }
}
