
#include <string>
#include <sstream>
#include <iostream>
#include <fstream>
#include <regex>
using namespace std;

int isLineValid(string line);

int main()
{

    ifstream myflux("data.txt");

    int summ = 0;
    if (myflux)
    {
        string line;
        int cmp = 1;
        while (getline(myflux, line))
        {
            int index = 1;
            for (char s : line)
            {
                if (s == ':')
                {
                    break;
                }
                ++index;
            }

            cout << cmp << endl;

            string line_sub = line.substr(index, line.size());
            // if (isLineValid(line_sub))
            // {
            //     summ += cmp;
            // }
            // ++cmp;

            summ += isLineValid(line_sub);
        }

        cout << summ << endl;
    }

    return 0;
}

int isLineValid(string line)
{

    stringstream ss(line);

    string t;

    char del = ';';

    int biggestBlue = 0;
    int biggestRed = 0;
    int biggestGreen = 0;

    while (std::getline(ss, t, del))
    {

        stringstream ss2(t);

        string w;

        char del2 = ',';

        while (getline(ss2, w, del2))
        {

            regex pattern("(\\d+)|(\\w+)");

            smatch match;

            string word;
            int number;

            while (regex_search(w, match, pattern))
            {

                if (match[1].matched)
                {

                    number = stoi(match[1].str());
                }
                else if (match[2].matched)
                {
                    word = match[2].str();
                }

                // move next part of string
                w = match.suffix().str();
            }

            if (word == "blue")
            {
                if (number > biggestBlue)
                {
                    biggestBlue = number;
                }
            }
            else if (word == "red")
            {
                if (number > biggestRed)
                {
                    biggestRed = number;
                }
            }
            else if (word == "green")
            {

                if (number > biggestGreen)
                {
                    biggestGreen = number;
                }
            }
        }
    }

    return (biggestBlue * biggestGreen * biggestRed);
}
