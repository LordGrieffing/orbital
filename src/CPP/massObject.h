#pragma once

#include <array>
#include <vector>
#include <cmath>
#include <tuple>


// helper functions
bool isOffsetZero(const std::array<double,3> offset);
double magnitude(const std::array<double, 3>& vec);
std::array<double, 3> addArray(const std::array<double, 3>& arr1, const std::array<double, 3>& arr2);
std::array<double, 3> arrayScale(const std::array<double, 3>& arr1, double scalar);


// massObject class declaration
class massObject{
    public:

        // public attributes
        double mass;
        std::array<double, 3> position;
        std::array<double, 3> velocity;
        double objectRadius;

        // Constructor
        massObject(double m, const std::array<double, 3>& p, const std::array<double, 3>& v, double r);

        // public functions
        std::array<double, 3> accelerate(const std::vector<massObject*> objects, const std::array<double, 3>& offset = {0,0,0}, bool RK = false);
        std::tuple<std::array<std::array<double, 3>, 4>, std::array<std::array<double, 3>,4>> kUpdate(const std::vector<massObject*> objects, int dt);
        void posVelUpdate(const std::array<std::array<double, 3>,4>& kVel, const std::array<std::array<double, 3>,4>& kPos, int dt);

    private:

        // Private attributes
        double G = 6.674 * pow(10, -11);
};