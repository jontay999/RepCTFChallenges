#include <iostream>
#include <unordered_map>
#include <ctime>
#include <string>
#include <vector>
using namespace std;

string flag = "REP{FAKE_FLAG}";

// Taken straight from https://leetcode.com/problems/two-sum/solution/
// C++ Two-pass Hash Table
class Solution
{
public:
    static void two_sum(vector<long long> &nums, long long target)
    {
        unordered_map<long long, long long> hash;
        for (int i = 0; i < nums.size(); i++)
        {
            hash[nums[i]] = i;
        }
        for (int i = 0; i < nums.size(); i++)
        {
            long long complement = target - nums[i];
            if (hash.find(complement) != hash.end() && hash[complement] != i)
            {
                cout << "Two sum indices: " << i << ", " << hash[complement] << "\n";
                return;
            }
        }
        cout << "No two sum solution could be found!\n";
    }
};

void print_menu()
{
    cout << "Menu:\n";
    cout << "1. Take in input \n";
    cout << "2. Run your input against my 2 sum solution \n";
    cout << "3. Exit \n";
}

void run_two_sum(vector<long long> &numbers)
{
    clock_t begin = clock();
    // Let me make sure that I always have a valid answer
    long long target = numbers.front() + numbers.back();
    Solution::two_sum(numbers, target);
    double time = (double)(clock() - begin) / CLOCKS_PER_SEC;
    cout << "The total time is " << time << "\n";
    if (time > 2.5)
    {
        cout << "how did you do that? \n";
        cout << flag << "\n";
    }
}

void receive_input(vector<long long> &all_numbers)
{
    int max_input_size = 10;
    cout << "Enter 10 space-separated numbers:\n";
    int num = 0;
    for (int i = 0; i < max_input_size; ++i)
    {
        cin >> num;
        all_numbers.push_back(num);
    }
}

int main()
{
    // Just to make the I/O faster
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    setbuf(stdin, 0);
    setbuf(stdout, 0);

    int remaining_inputs = 1000;
    vector<long long> all_numbers;
    int choice;
    while (true)
    {
        print_menu();
	cout << "Remaining Inputs: " << remaining_inputs << "\n";
        cin >> choice;
        switch (choice)
        {
        case 1:
            if (remaining_inputs-- <= 0)
            {
                cout << "You have reached the maximum number of inputs.\n";
                cout << "Exiting...\n";
                exit(0);
            }
            receive_input(all_numbers);
            break;
        case 2:
            if (all_numbers.size() < 2)
            {
                cout << "You need at least 2 numbers in your array. Please use option 1 to enter numbers first.\n";
                break;
            }
            else
            {
                cout << "Running my two_sum solution against your input of " << all_numbers.size() << " numbers\n";
                run_two_sum(all_numbers);
                return 0;
            }
        case 3:
            cout << "Exiting...\n";
            return 0;
        default:
            cout << "Invalid option. Please try again.\n";
        }
    }
}
