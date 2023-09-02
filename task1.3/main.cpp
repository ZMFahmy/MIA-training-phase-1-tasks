#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    int choice;
    vector<string> tasks;
    cout << "Minions Task Manager" << endl;
    cout << "1. Add Task" << endl;
    cout << "2. View Tasks" << endl;
    cout << "3. Remove Task" << endl;
    cout << "4. Exit" << endl;
    label:
    cout << endl << "Select an option: ";
    cin >> choice;
    cout << endl;

    string description;
    int task_removed;
    vector<int>::iterator it;

    switch(choice)
    {
    case 1:
        cout << "Enter task description: ";
        cin.ignore();
        getline(cin, description);
        tasks.push_back(description);
        cout << "Task added successfully!" << endl << endl;
        break;
    case 2:
        cout << "Current tasks:" << endl;
        for(int i = 0; i<tasks.size(); i++)
        {
            cout << "Task ID: " << i + 1 << endl;
            cout << "Description: " << tasks[i] << endl << endl;
        }
        break;
    case 3:
        cout << "Enter task ID to remove: ";
        cin >> task_removed;
        if(task_removed > tasks.size() || task_removed < 1)
            cout << "No such task !!" << endl << endl;
        else
        {
            for(int i = task_removed -1; i < tasks.size() - 1; i++)
                tasks.at(i) = tasks[i + 1];
            tasks.pop_back();
            cout << "Task removed successfully" << endl << endl;
        }
        break;
    case 4:
        cout << "Exiting Minions Task Manager. Have a great day!" << endl;
        return 0;
        break;
    default:
        cout << "Unknown command..." << endl << endl;

        break;
    }
    goto label;

    return 0;
}
