#include <iostream>
#include <unordered_map>
#include <ctime>
#include <string>
#include <vector>
using namespace std;

#define LIMIT 25000

string flag = "REP{FAKE_FLAG}";

// Taken straight from https://leetcode.com/problems/two-sum/solution/
// C++ Two-pass Hash Table
class Solution
{
public:
    static vector<int> two_sum(vector<int> &nums, int target)
    {
        unordered_map<int, int> hash;
        for (int i = 0; i < nums.size(); i++)
        {
            hash[nums[i]] = i;
        }
        for (int i = 0; i < nums.size(); i++)
        {
            int complement = target - nums[i];
            if (hash.find(complement) != hash.end() && hash[complement] != i)
            {
                return {i, hash[complement]};
            }
        }
        return {};
    }
};

void print_menu()
{
    cout << "Menu:\n";
    cout << "1. Take in input: \n";
    cout << "2. Run your input against my 2 sum solution: \n";
    cout << "3. Exit\n";
}

void receive_input(vector<int> &all_numbers)
{
    int max_input_size = 1000;
    cout << "Enter 1000 space-separated numbers:\n";
    int num = 0;
    for (int i = 0; i < max_input_size; ++i)
    {
        cin >> num;
        all_numbers.push_back(num);
    }
}

void run_two_sum(vector<int> &numbers)
{
    clock_t begin = clock();
    // Let me make sure that I always have a valid answer
    int target = numbers.front() + numbers.back();
    vector<int> result = Solution::two_sum(numbers, target);

    if (!result.empty())
        cout << "Indices: " << result[0] << " and " << result[1] << endl;
    else
        cout << "No two sum solution found." << endl;

    double time = (double)(clock() - begin) / CLOCKS_PER_SEC;
    cout << "The total time is " << time << "\n";
    if (time > 5.0)
    {
        cout << "how did you do that? \n";
        cout << flag << "\n";
    }
}

int main()
{
    // Ignore these two lines
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int input_count = 0;
    const int max_inputs = 20;
    vector<int> all_numbers;
    int choice;
    while (true)
    {
        print_menu();
        cin >> choice;
        switch (choice)
        {
        case 1:
            if (input_count >= max_inputs)
            {
                cout << "You have reached the maximum number of inputs.\n";
                cout << "Exiting...\n";
                exit(0);
            }
            receive_input(all_numbers);
            input_count++;
            break;
        case 2:
            if (all_numbers.size() < 2)
                cout << "You need at least 2 numbers in your array. Please use option 1 to enter numbers first.\n";
            else
            {
                cout << "Running my two_sum solution against your input of " << all_numbers.size() << " numbers\n";
                run_two_sum(all_numbers);
            }
            return 0;

        case 3:
            cout << "Exiting...\n";
            return 0;
        default:
            cout << "Invalid option. Please try again.\n";
        }
    }
}