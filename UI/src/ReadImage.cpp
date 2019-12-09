#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <string>
#include <regex>

#include "../include/image.h"

#define DEBUGGING false

using namespace std;

const string FORMAT_ERROR_MSG = "Something went wrong while reading the file: it appears to have the wrong format (for a PGM file)!";

void skipWhitespaces(ifstream & fin) {
	while(true) {
		auto c = fin.peek();
		if(isspace(c)) {
			fin.get();
		} else {
			break;
		}
	}
}

void skipCommentLines(ifstream & fin) {
	skipWhitespaces(fin);
	while(fin.peek() == '#') {
		if(DEBUGGING) {cout << "Read comment: ";}
		int c;
		while((c = fin.get()) != '\n') {
			if(DEBUGGING) {cout << (char)c;}
		}
		if(DEBUGGING) {cout << endl;}
		skipWhitespaces(fin);
	}
}

int readImage(string filename, Image & image) {
	ifstream fin(filename, ios::in | ios::binary);
	if(!fin) {
		cerr << "Can't read image: " << filename << endl;
		return -1;
	}
	
	skipCommentLines(fin);
	string fileType;
	fin >> fileType;
	if(fileType != "P5" && fileType != "P2") {
		cerr << FORMAT_ERROR_MSG << endl;
		cerr << "(The header contained \"" << fileType << "\")" << endl;
		return -1;
	}

	uint width, height;
	ubyte2 maxGray;
	skipCommentLines(fin);
	fin >> width;
	skipCommentLines(fin);
	fin >> height;
	skipCommentLines(fin);
	fin >> maxGray;
	if(DEBUGGING) {
		cout << "width: " << width << endl;
		cout << "height: " << height << endl;
		cout << "maxGray: " << maxGray << endl;
	}
	if(!fin) {
		cerr << FORMAT_ERROR_MSG << endl;
		return -1;
	}
	
	image.create(width, height, maxGray);

	uint y = 0, x = 0;
	for(y = 0; y < height; ++y) {
		skipCommentLines(fin);
		for(x = 0; x < width; ++x) {
			char pixel[2];
			pixel[1] = (char)((maxGray >> 8) ? fin.get() : 0);
			pixel[0] = (char)fin.get();
			image(x, y) = *reinterpret_cast<ubyte2 *>(pixel);
		}
	}

	if(!fin) {
		cerr << "There was a failure while reading the image pixels; perhaps the size is incorrect?" << endl;
		cerr << "Stopped at " << x  << "/" << width << "," << y << "/" << height << endl;
		return -1;
	}

	fin.close();
	return 0;
}
