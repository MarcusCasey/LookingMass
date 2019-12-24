#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <algorithm>
#include <math.h>

#include "../include/image.h"

using namespace std;

const float PI = 3.141592653589793238f;

//void sampling(Image, Image&, const int);

/*Image ProcessImage(const char filePath[] ) 
{
    bool type2;
    int Z, X, Y; // for image sampling
    const int FACTOR = 2; // Change this to make new size

    readImageHeader(filePath, Z, X, Y, type2);
    Image samplingImage(Z, X, Y);
    samplingImage.getImageInfo(Z, X, Y);

    int L = Z / FACTOR,
        O = X / FACTOR,
        P = Y;
    
    Image resizedImg(L, O, P);
    readImage(filePath, samplingImage);
    sampling(samplingImage, resizedImg, FACTOR);
    return resizedImg;
}*/

float distance(float x0, float y0, float x = 0, float y = 0) {
	float dx = x-x0, dy = y-y0;
	return sqrt(dx*dx + dy*dy);
}

void highlightPixel(ubyte2 & pixel, ubyte2 maxGray) {
	pixel = (ubyte2)((maxGray-pixel) * 0.5f + pixel);
}
void stripePixel(ubyte2 & pixel, float x, float y, float period = 10) {
	pixel = (ubyte2)(pixel * (sin((x+y)*2*PI/period) + 1)/2);
}

//Only for testing the prototype
void processImage(Image & image) {
	auto [width, height] = image.getDims();

	float radius = (float)min(width, height)/10 + 4;
	float thickness = radius/5 + 2;
	float centerX = (float)width/2, centerY = (float)height/2;

	for(uint y = 0; y < height; ++y) {
		for(uint x = 0; x < width; ++x) {
			float d = distance(centerX, centerY, (float)x, (float)y);
			if(d < radius-thickness/2) {
				highlightPixel(image(x, y), image.getMaxGray());
			} else if(d < radius+thickness/2) {
				stripePixel(image(x, y), (float)x, (float)y);
			} else {
				//Preserve pixel as-is
			}
		}
	}

}

/**
 *  Details: Take in an integer defining how much to sample the
 *            image, e.g. 2. Run through the pixel values and store
 *            every 2nd pixel value into a new array which will be the
 *            pixel values of the new image, or every 4th pixel, or 8th.
 * */
/*void sampling(Image srcImg, Image& newImg, const int FACTOR) {
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
}*/
