#include <ctime>
#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>
using namespace std;

const int N = 10000;
string flag = "REP{fake_flag}";

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

void run_two_sum(long long x)
{
    vector<long long> numbers;
    for (int i = 1; i <= N; i++)
        numbers.push_back(i * x);
    clock_t begin = clock();
    long long target = numbers.front() + numbers.back();
    Solution::two_sum(numbers, target);
    double time = (double)(clock() - begin) / CLOCKS_PER_SEC;
    printf("x = %lld: %.3lf seconds\n", x, (double)(clock() - begin) / CLOCKS_PER_SEC);
}

int main()
{
    vector<long long> primes = {20753, 10273};
    for (int i = 0; i < primes.size(); i++)
    {
        run_two_sum(primes[i]);
    }
}
