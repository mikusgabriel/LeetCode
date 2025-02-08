
#include <string>
#include <sstream>
#include <iostream>
#include <fstream>
#include <regex>
#include <unordered_map>
#include <vector>
using namespace std;

// how the fuck do i not use that but wtv
struct pair_hash
{
    template <class T1, class T2>
    size_t operator()(const pair<T1, T2> &p) const
    {
        auto hash1 = hash<T1>{}(p.first);
        auto hash2 = hash<T2>{}(p.second);
        return hash1 ^ (hash2 << 1); // Combine the two hashes
    }
};

int getSummNumbers(unordered_map<pair<int, int>, int, pair_hash> &map, const vector<pair<int, int>> &symbols)
{

    for (const auto &item : map)
    {
        cout << "(" << item.first.first << ", " << item.first.second << ") -> " << item.second << endl;
    }

    for (const auto &item : symbols)
    {
        cout << "(" << item.first << ", " << item.second << ")" << endl;
    }

    int summ = 0;

    vector<vector<int>> listPossibilities = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}, {1, 1}, {-1, -1}, {1, -1}, {-1, 1}};

    for (const auto &item : symbols)
    {
        for (vector<int> possibility : listPossibilities)
        {

            int temp_x = item.first + possibility.at(0);
            int temp_y = item.second + possibility.at(1);

            if (map.count(make_pair(temp_x, temp_y)))
            {
                cout << temp_x << " " << temp_y << " " << map[make_pair(temp_x, temp_y)] << endl;
                summ += map[make_pair(temp_x, temp_y)];
            }
        }
    }

    return summ;
}

int main()
{

    ifstream my_flux("data.txt");

    if (my_flux)
    {

        string line;
        int height;
        int lenght;

        int y = 0;

        vector<pair<int, int>> listSymbol;
        unordered_map<pair<int, int>, int, pair_hash> map;

        while (getline(my_flux, line))
        {

            int number_cmp = 0;
            bool numberFound = false;
            string number = "";

            for (int x = 0; x < line.size(); x++)
            {
                if (!numberFound)
                {
                    number = "";
                }

                if (line.at(x) != '.')
                {

                    if (isdigit(line.at(x)))
                    {
                        if (numberFound)
                        {

                            map.insert(make_pair(make_pair(x, y), stoi(number)));
                            --number_cmp;
                            if (number_cmp == 0)
                            {
                                numberFound = false;
                            }
                        }
                        else
                        {
                            // iterates till find not number

                            int temp_number = x;
                            while (line.at(temp_number) != '.' && temp_number < line.size())
                            {
                                if (isdigit(line.at(temp_number)))
                                {
                                    number += line.at(temp_number);
                                }
                                ++temp_number;
                            }
                            number_cmp = temp_number - x;
                            if (number_cmp == 0)
                            {
                                cout << "problem" << endl;
                            }
                            // ----
                            map.insert(make_pair(make_pair(x, y), stoi(number)));
                        }
                    }
                    else
                    {
                        listSymbol.push_back(make_pair(x, y));
                        numberFound = false;
                    }
                }
                else
                {
                    numberFound = false;
                }
            }

            ++y;
        }

        cout << getSummNumbers(map, listSymbol) << endl;
    }

    return 0;
}

// doit changer la logique de mettre chaque nombre a sa position maybe regex
