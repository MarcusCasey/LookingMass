#include <iostream>
#include "../include/image.h"

using namespace std;

int writeImage(const char[], ImageType&);
ImageType ProcessImage(const char[]);

void MainMenu();
// Since MainMenu is recursively checking made fileName global because it wasn't storing it.
string fileName;
ImageType newImage;
const char* inputName = "./data_input/lenna_1.pgm";
const char* outputName = "./data_output/TEST.pgm";


int main(int argc, char *argv[])
{
  MainMenu();

  return 0;
}

void MainMenu()
{

  char selection;

  cout << "\n Menu";

  cout << "\n========";

  cout << "\n 1 - Load an image for analysis";

  cout << "\n 2 - Resize image";

  cout << "\n 3 - Save modified image";

  cout << "\n 4 - Exit";

  cout << "\n Enter selection: ";

  // read the input

  cin >> selection;

  // string fileName;
  switch (selection)
  {
    case '1':
    {
      // cout << "filename:" << fileName;
      
      cout << "\n Enter image name + file type: ";
      cin >> fileName;
      cout << "\n File Loaded!\n";
      //LoadImage();
      MainMenu();
    }

    case '2':
    {
      cout << "\n Running Detection Algorithm....";
      newImage = ProcessImage(inputName);

      cout << "\n Complete!";

      MainMenu();
    }

    case '3':
    {
      cout << "\n Image Saved To Base Folder";

      //SaveImage();
      writeImage(outputName, newImage);
      MainMenu();
    }

    case '4':
    {
      cout << "\n Exiting...";
    }
    break;

    default:
      cout << "\n Invalid selection";

      // no break in the default case
    }

    cout << "\n";
}
