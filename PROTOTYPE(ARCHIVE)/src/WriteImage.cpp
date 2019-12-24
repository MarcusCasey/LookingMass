#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <string>

#include "../include/image.h"

using namespace std;
using uint = unsigned int;

int writeImage(string filename, const Image & image) {
	auto [width, height] = image.getDims();
	if(width*height == 0) {
		cerr << "The image is empty, nothing to write!" << endl;
		return -1;
	}
	ubyte2 maxGray = image.getMaxGray();

	ofstream fout(filename, ios::out | ios::binary);
	if(!fout) {
		cerr << "Can't open file: " << filename << endl;
		return -1;
	}
	
	fout << "P5" << endl;
	fout << width << " " << height << endl;
	fout << maxGray << endl;
	
	//Each pixel may be written as either 1 or 2 bytes, depending on size of maxGray
	for(uint y = 0; y < height; ++y) {
		for(uint x = 0; x < width; ++x) {
			//Break up each pixel value into two chars
			char pixel[2];
			pixel[1] = image(x, y) >> 8;
			auto test = image(x, y) & ((1 << 8) - 1);
			pixel[0] = image(x, y) & ((1 << 8) - 1);
			//Omit second byte of pixel if maxGray takes up less than a byte
			fout.write(pixel, (maxGray >> 8) ? 2 : 1);
		}
	}
	
	if(fout.fail()) {
	  cerr << "Can't write image " << filename << endl;
	  return -1;
	}
	
	fout.close();
	return 0;
}
