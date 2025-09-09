#include <iostream>
#include <string>
#include <cstdlib>
#include <fstream>

using namespace std;

const string USER_FILE = "user.txt";

void user();
void wait();
void clear();
void menu();

void user() {
    system("./bash/welcome.sh");
    string user;
    ifstream userFile(USER_FILE);
    if (userFile) {
        getline(userFile, user);
        userFile.close();
        string notification = "notify-send \"Welcome back to Luna, " + user + "\"";
        system(notification.c_str());
    } else {
        cout << "[+] Enter your user: ";
        cin >> user;
        ofstream userFileOut(USER_FILE);
        userFileOut << user;
        userFileOut.close();
        string notification = "notify-send \"Welcome to Luna, " + user + "\"";
        system(notification.c_str());
    }
}

void wait() {
    cout << "\nPress Enter to return to the menu...";
    cin.ignore();
    cin.get();
}

void clear() {
    system("clear");
}

void menu() {
    clear();
    user();
    string banner = R"(
                                       ▄█       ███    █▄  ███▄▄▄▄      ▄████████ 
                                      ███       ███    ███ ███▀▀▀██▄   ███    ███ 
                                      ███       ███    ███ ███   ███   ███    ███ 
                                      ███       ███    ███ ███   ███   ███    ███ 
                                      ███       ███    ███ ███   ███ ▀███████████ 
                                      ███       ███    ███ ███   ███   ███    ███ 
                                      ███▌    ▄ ███    ███ ███   ███   ███    ███ 
                                      █████▄▄██ ████████▀   ▀█   █▀    ███    █▀  
                                      ▀           
                                             github: https://github.com/Moon0day/

                                             1. nmap commands
                                             2. sqlmap commands
                                             3. discord bot (cybersecurity)
                                             4. exit
    )";
    cout << banner;
    string choice;
    cout << "\n[=] Enter choice: ";
    getline(cin, choice);
    if (choice == "1") {
        clear();
        system("python3 nmap.py");
        wait();
        menu();
    } else if (choice == "2") {
        clear();
        system("python3 sqlmap.py");
        wait();
        menu();
    } else if (choice == "3") {
        clear();
        system("./src/env");
        system("python3 discord.py");
        wait();
        menu();
    } else if (choice == "4") {
        clear();
        cout << "\nExiting...\n";
    } else {
        cout << "\nInvalid choice, try again.\n";
        wait();
        menu();
    }
}

int main() {
    system("notify-send \"Lunaris\" \"Welcome<33\"");
    clear();
    menu();
    return 0;
}
