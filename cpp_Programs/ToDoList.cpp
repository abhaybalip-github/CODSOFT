// cpp program
// console based to-do list
#include <iostream>
#include <math.h>
#include <vector>
#include <map>
#include <iterator>

// map data structure for storing list
std::map<int, std::string> Task_List;
// list handeling function
void Add_Item(std::string task)
{
    Task_List.insert({Task_List.size() + 1, task});
}
void Remove_Item(int key)
{
    Task_List.erase(key);
}
void Display_List()
{
    for (std::iterator<int, std::string> itr = Task_List.begin(); itr < Task_List.end(); itr++)
    {
    }
}
int main(int argc, char const *argv[])
{
    /* code */

    return 0;
}
