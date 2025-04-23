#include <array>
#include <vector>
#include <cmath>
#include <tuple>
#include <iostream>
#include "massObject.h"


int main(){

    // Declare state/universal variables
    int dt = 30;
    int simSteps = 2000;

    // Declare mass objects
    double eM = 5.97219 * pow(10, 24);
    std::array<double, 3> ePos = {0,0,0};
    std::array<double, 3> eVel = {0,0,0};
    double eRadius = 6377993.2066;

    double sM = 10;
    std::array<double, 3> sPos = {2000000 + eRadius,0,0};
    std::array<double, 3> sVel = {0,7210,0};
    double sRadius = 5;

    massObject earth(eM, ePos, eVel, eRadius);
    massObject satellite(sM, sPos, sVel, sRadius);

    // Declare storage variables
    std::vector<std::array<double,3>> earthPath;
    std::vector<std::array<double,3>> satePath;

    // Declare RungeKutta constant arrays
    std::array<std::array<double, 3>,4> earthKVel;
    std::array<std::array<double, 3>,4> sateKVel;

    std::array<std::array<double, 3>,4> earthKPos;
    std::array<std::array<double, 3>,4> sateKPos;

    // Objects vector
    std::vector<massObject*> objects = {&earth, &satellite};


    // Calculate positions
    for(int i = 0; i < simSteps; i++){

        // record current position
        earthPath.push_back(earth.position);
        satePath.push_back(satellite.position);

        // Get the K constants for this step
        std::tie(earthKVel, earthKPos) = earth.kUpdate(objects, dt);
        std::tie(sateKVel, sateKPos) = satellite.kUpdate(objects, dt);

        // Update positions and velocities of the objects
        earth.posVelUpdate(earthKVel, earthKPos, dt);
        satellite.posVelUpdate(sateKVel, sateKPos, dt);
    }
    

    // Print positions
    for(int i = 0; i < satePath.size(); i++){
        std::cout << "Step " << i << ": (" 
                  << satePath[i][0] << ", "
                  << satePath[i][1] << ", "
                  << satePath[i][2] << ") " << std::endl;
    }


    return 0;
}