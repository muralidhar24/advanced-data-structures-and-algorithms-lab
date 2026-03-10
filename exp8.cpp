#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Job {
    char id;
    int deadline;
    int profit;
};

bool compare(Job a, Job b) {
    return a.profit > b.profit; // Sort in descending order of profit
}

void jobSequencing(vector<Job>& jobs) {
    int n = jobs.size(), i, j;

    // Sort jobs by profit
    sort(jobs.begin(), jobs.end(), compare);

    // Find maximum deadline to size the slot array
    int maxDeadline = 0;
    for (i = 0; i < n; i++)
        maxDeadline = max(maxDeadline, jobs[i].deadline);

    vector<int> slot(maxDeadline + 1, -1); // -1 means slot is free
    vector<char> result(maxDeadline + 1, ' '); // Store job IDs
    int totalProfit = 0;

    for (i = 0; i < n; i++) {
        for (j = jobs[i].deadline; j > 0; j--) {
            if (slot[j] == -1) {
                slot[j] = i;
                result[j] = jobs[i].id;
                totalProfit += jobs[i].profit;
                break;
            }
        }
    }

    cout << "Scheduled Jobs: ";
    for (i = 1; i <= maxDeadline; i++) {
        if (result[i] != ' ')
            cout << result[i] << " ";
    }
    cout << "\nTotal Profit: " << totalProfit << endl;
}

int main() {
    vector<Job> jobs = {
        {'A', 2, 100},
        {'B', 1, 19},
        {'C', 2, 27},
        {'D', 1, 25},
        {'E', 3, 15}
    };

    jobSequencing(jobs);

    return 0;
}


