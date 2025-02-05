
#include <iostream>
#include <string>
#include <fstream>
#include <regex>
#include <map>

#include <list>
using namespace std;

string changeLine(string line)
{

  map<string, string> numberMap = {
      {"1", "one"},
      {"2", "two"},
      {"3", "three"},
      {"4", "four"},
      {"5", "five"},
      {"6", "six"},
      {"7", "seven"},
      {"8", "eight"},
      {"9", "nine"}};

  for (auto kv : numberMap)
  {

    line = regex_replace(line, regex(kv.second), kv.second.substr(0, int(kv.second.size() / 2)) + kv.first + kv.second.substr(int((kv.second.size() / 2) + 1), kv.second.size() - 1));
  }

  return line;
}

int main()
{

  int summ = 0;
  ifstream myflux("data.txt");

  if (myflux)
  {
    string line;
    while (getline(myflux, line))
    {

      cout << line << endl;

      line = changeLine(line);

      cout << line << endl;

      regex digit_regex("[0-9]");
      sregex_iterator it(line.begin(), line.end(), digit_regex);
      sregex_iterator end_it;

      string first_one = it->str();

      sregex_iterator last_it = it;
      while (++it != end_it)
      {
        last_it = it;
      }

      string last_one = last_it->str();

      int total = stoi(first_one + last_one);
      cout << total << endl;
      summ += total;
    }
  }

  cout << summ;

  return 0;
}
