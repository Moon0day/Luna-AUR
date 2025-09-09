
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

const string ENV_FILE = ".env";

void handle_env() {
    string line;
    ifstream envFile(ENV_FILE);

    if (envFile) {
        getline(envFile, line);
        envFile.close();
        cout << "Token from .env: " << line << endl;
    } else {
        string token;
        cout << "Enter your token: ";
        getline(cin, token);

        ofstream envFileOut(ENV_FILE);
        envFileOut << "token=" << token << endl;
        envFileOut.close();

        cout << "Token saved to .env file." << endl;
    }
}
