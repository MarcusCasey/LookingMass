#ifndef IMAGE_H
#define IMAGE_H
using namespace std;

class ImageType {
 public:
   ImageType();
   ImageType(int, int, int);
   ImageType(ImageType&);
   ~ImageType();
   void getImageInfo(int&, int&, int&);
   void setImageInfo(int, int, int);
   void setPixelVal(int, int, int);
   void getPixelVal(int, int, int&);
   ImageType& operator= (const ImageType& other);

 private:
   int N, M, Q;
   int **pixelValue;
};

#endif
