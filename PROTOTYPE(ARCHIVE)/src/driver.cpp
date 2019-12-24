#include <iostream>
#include <string>
#include <sstream>
// #include <experimental/filesystem>

#include "../include/image.h"
#include "../include/WriteImage.h"
#include "../include/ReadImage.h"
#include "../include/ProcessImage.h"

using namespace std;

void mainMenu();

string fileName;
Image globalImage;
const string inputDirectory = "./data_input/";
const string defaultInputFilename = "lenna_1.pgm";
const string outputDirectory = "./data_output/";
const string defaultOutputFilename = "TEST.pgm";

void listDirectoryFiles(string directory) {
	// for(const auto & entry : std::experimental::filesystem::directory_iterator(directory)) {
	// ss << entry.path().filename();
	stringstream ss;
	ss << inputDirectory + defaultInputFilename;
	string filename = ss.str();
	filename = filename.substr(1, filename.size()-2);
	cout << "\t" << filename << endl;
	// }
}

int main(/*int argc, char *argv[]*/) {
	mainMenu();
	return 0;
}

void mainMenu() {
	bool running = true;

	while(running) {
		char selection;
		
		cout << "Menu" << endl;
		cout << "========" << endl;
		cout << "0 - Exit" << endl;
		cout << "1 - List available images" << endl;
		cout << "2 - Load an image" << endl;
		cout << "3 - Process current image" << endl;
		cout << "4 - Save current image" << endl;
		cout << "Enter selection: ";
		
		cin >> selection;
		cin.ignore(numeric_limits<streamsize>::max(), '\n');
		cout << endl;

		string filename;

		switch(selection) {
			case '0':
				cout << "Exiting..." << endl;
				running = false;
				break;
			case '1':
				cout << "Files in " << inputDirectory << ":" << endl;
				listDirectoryFiles(inputDirectory);
				break;
			case '2':
				cout << "Enter image name (with extension) or leave empty to load default: ";
				//filename = "";
				//cin >> filename;
				char buffer[256];
				cin.getline(buffer, 256);
				filename = buffer;
				if(readImage(inputDirectory + ((filename == "") ? defaultInputFilename : filename), globalImage) >= 0) {
					cout << "File Loaded!" << endl;
				}
				break;
			case '3':
				cout << "Processing image...." << endl;
				processImage(globalImage);
				cout << "Complete!" << endl;
				break;
			case '4':
				if(writeImage(outputDirectory + defaultOutputFilename, globalImage) >= 0) {
					cout << "Image saved!" << endl;
				}
				break;
			default:
				cout << "Invalid selection" << endl;
		}
		cout << endl << endl;
	}
}
