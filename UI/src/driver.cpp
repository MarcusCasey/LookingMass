#include <iostream>
#include <string>

#include "../include/image.h"

using namespace std;

void ProcessImage();
int writeImage(const char[], ImageType&);
void MainMenu();
ImageType ProcessImage(const char[]);

string fileName;
ImageType newImage;
const char* inputName = "./data_input/lenna_1.pgm";
const char* outputName = "./data_output/TEST.pgm";


int main(int argc, char *argv[]) {
	MainMenu();
	return 0;
}

void MainMenu() {
	while(true) {
		char selection;
		
		cout << "Menu" << endl;
		cout << "========" << endl;
		cout << "1 - Load an image for analysis" << endl;
		cout << "2 - Check for gravitational lensing" << endl;
		cout << "3 - Save modified image" << endl;
		cout << "4 - Exit" << endl;
		cout << "Enter selection: ";
		
		cin >> selection;
		string fileName;

		switch (selection) {
			case '1':
				cout << "Enter image name (with extension): ";
				cin >> fileName;
				if(LoadImage()) {
					cout << "File Loaded!" << endl;
				}
				MainMenu();
				break;

			case '2':
				cout << "Running Detection Algorithm...." << endl;
				ProcessImage();
				cout << "Complete!" << endl;
				MainMenu();
				break;
			
			case '3':
				cout << "Image Saved To Base Folder" << endl;
				SaveImage();
				MainMenu();
				break;
			
			case '4':
				cout << "Exiting..." << endl;
				break;
			
			default:
				cout << "Invalid selection" << endl;
		}
	}
}
