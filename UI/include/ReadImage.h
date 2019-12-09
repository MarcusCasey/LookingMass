#ifndef READ_IMAGE_H
#define READ_IMAGE_H

#include <string>
#include <fstream>

#include "image.h"

bool skipCommentLines(std::ifstream & fin);
int readImage(std::string filename, Image & image);

#endif /*READ_IMAGE_H*/