#include <stdlib.h>

#include "../include/image.h"

Image::Image() {
	height = width = 0;
	maxGray = 0;
	pixels = nullptr;
}

Image::Image(Image & other) {
	height = other.height;
	width = other.width;
	maxGray = other.maxGray;
	
	pixels = new ubyte2[height*width];
	for(uint y = 0; y <height; ++y) {
		for(uint x = 0; x < width; ++x) {
			(*this)(x, y) = other(x, y);
		}
	}
}

Image::~Image() {
	reset();
}


DIMS Image::getDims() const {
	return {width, height};
}
/*void Image::setDims(uint width_, uint height_) {
	width = width_;
	height = height_;
}*/

ubyte2 Image::getMaxGray() const {
	return maxGray;
}
/*void Image::setMaxGray(ubyte2 maxGray_) {
	maxGray = maxGray_;
}*/

ubyte2 & Image::operator()(uint x, uint y) {
	return pixels[x + width*y];
}
const ubyte2 & Image::operator()(uint x, uint y) const {
	return pixels[x + width * y];
}

void Image::reset() {
	width = height = 0;
	if(pixels) {
		delete[] pixels;
	}
	pixels = nullptr;
}
void Image::create(uint width_, uint height_, ubyte2 maxGray_) {
	reset();

	width = width_;
	height = height_;
	maxGray = maxGray_;

	pixels = new ubyte2[height*width];
}

Image & Image::operator=(const Image& other) {
  height = other.height;
  width = other.width;
  maxGray = other.maxGray;

  pixels = new ubyte2[width*height];

  for(uint y = 0; y < height; ++y) {
	  for(uint x = 0; x < width; ++x) {
		  (*this)(x, y) = other(x, y);
	  }
  }
  return *this;
}

