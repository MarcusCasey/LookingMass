#include <iostream>
#include <string>

using namespace std;

void ProcessImage();
void MainMenu();

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
				cout << "\n Image Saved To Base Folder";
				SaveImage();
				MainMenu();
				break;
			
			case '4':
				cout << "\n Exiting...";
				break;
			
			default:
				cout << "\n Invalid selection";
		}
	}
}
