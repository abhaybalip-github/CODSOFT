// cpp program
// console based to-do list
#include <iostream>
#include <math.h>
#include <vector>
#include <map>
#include <iterator>

std::vector<std::string> task_list;
std::vector<bool> task_status;
bool close = false;
void insert_task(std::string task)
{
    task_list.push_back(task);
    task_status.push_back(1);
    std::cout << "Task Added \n\n";
}
void delete_task(int key)
{
    if (task_list.size() > 0)
    {
        task_list.erase(task_list.begin() + key - 1);
        std::cout << "Task Removed \n\n";
    }
    else
    {
        std::cout << "No Task Avaliable \n\n";
    }
}
void display_task()
{
    if (task_list.size() > 0)
    {
        std::cout << "No.\tStatus\tTask\n";
        for (int i = 0; i < task_list.size(); i++)
        {
            /* code */
            std::cout << i + 1 << "\t";
            task_status[i] ? std::cout << "Active  \t" : std::cout << "InActive\t";
            std::cout << task_list[i] << " \n";
        }
    }
    else
    {
        std::cout << "No Task Avaliable \n\n";
    }
}
int main(int argc, char const *argv[])
{
    /* code */
    while (!close)
    {
        /* code */
        if ()
    }

    return 0;
}
