
#include <iostream>
#include <string>
using namespace std;

int main() {
    string user;

    cout << "Welcome to AI Chatbot" << endl;
    cout << "Type 'bye' to exit" << endl;

    while (true) {
        cout << "You: ";
        getline(cin, user);

        for (char &c : user)
            c = tolower(c);

        if (user == "hi" || user == "hello") {
            cout << "Bot: Hello! How can I help you?" << endl;
        }
        else if (user == "how are you") {
            cout << "Bot: I am fine. Thank you!" << endl;
        }
        else if (user == "what is your name") {
            cout << "Bot: My name is AI Chatbot." << endl;
        }
        else if (user == "what is ai") {
            cout << "Bot: AI means Artificial Intelligence." << endl;
        }
        else if (user == "help") {
            cout << "Bot: I can answer simple questions." << endl;
        }
        else if (user == "thanks" || user == "thank you") {
            cout << "Bot: You're welcome!" << endl;
        }
        else if (user == "bye") {
            cout << "Bot: Goodbye!" << endl;
            break;
        }
        else {
            cout << "Bot: Sorry, I don't understand." << endl;
        }
    }

    return 0;
}
