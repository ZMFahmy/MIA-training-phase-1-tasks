#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<float> sensor_1 = {0.0, 11.68, 18.95, 23.56, 25.72, 25.38, 22.65, 18.01, 10.14, -0.26};
    vector<float> sensor_2 = {0.0,9.49, 16.36, 21.2, 23.16, 22.8, 19.5, 14.85, 6.79, -2.69};
    vector<float> output;

    for(int i = 0; i < sensor_1.size(); i++)
    {
        float avg = (0.79 * sensor_1[i] + 0.92 * sensor_2[i]) / 2;
        output.push_back(avg);
    }

    cout << "Average:" << endl << "[" << endl;
    for(int i = 0; i < output.size(); i++)
        cout << output[i] << endl;
    cout << "]";

    return 0;
}
